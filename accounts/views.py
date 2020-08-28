from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from .forms import ProfileForm
from news.models import News
from .models import Switcher


def index(request):
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('switcher'))
            else:
                login_form.add_error(None, 'your u or p is wrong')
    else:
        login_form = UserLoginForm()
    return render(request, 'index.html', {'login_form': login_form})


@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect('index')

# def login(request):
#     """Return a login page"""
#     if request.user.is_authenticated:
#         return redirect(reverse('index'))
#     if request.method == "POST":
#         login_form = UserLoginForm(request.POST)
#         if login_form.is_valid():
#             user = auth.authenticate(username=request.POST['username'],
#                                      password=request.POST['password'])

#             if user:
#                 auth.login(user=user, request=request)
#                 messages.success(request, "You have successfully logged in")
#                 """return redirect(reverse('index'))"""
#             else:
#                 login_form.add_error(None, 'your u or p is wrong')
#     else:
#         login_form = UserLoginForm()
#     return render(request, 'login.html', {'login_form': login_form})


def registration(request):

    # if request.method == "POST":
    #     registration_form = UserRegistrationForm(request.POST)
    #     profile_form = ProfileForm(request.POST)

    #     if registration_form.is_valid() and profile_form.is_valid():
    #         xe = registration_form.save()
    #         xe.profile.telephone = "testing"
    #         xe.save()

    registration_form = UserRegistrationForm()
    profile_form = ProfileForm()
    return render(request, 'registration.html', {'registration_form': registration_form, 'profile_form': profile_form})


def user_profile(request):
    """the users profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {'profile': user})


@login_required
def dashboard(request):
    user = request.user
    articles = News.objects.all()[:3]
    switchData = Switcher.objects.filter(user=user)

    return render(request, 'dashboard.html', {'articles': articles,  'switchData': switchData})


def switcher(request):

    # set user id
    user = request.user
    # filters switcher table by user
    switchData = Switcher.objects.filter(user=user)
    # queries first instance in list
    grp = switchData[0].group.pk
    bp = switchData[0].business_profile.pk

    # set business profile and group cookies
    request.session['group'] = grp
    request.session['bussprof'] = bp

    return redirect(reverse('dashboard'))


def switching(request, pk):
    # changes the group and business based on the switcher instance by updating session cookies
    switchdata = Switcher.objects.get(pk=pk)
    grp = switchdata.group.pk
    bp = switchdata.business_profile.pk
    request.session['group'] = grp
    request.session['bussprof'] = bp
    return redirect(reverse('dashboard'))

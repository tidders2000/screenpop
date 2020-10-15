from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from .forms import ProfileForm, switcher_form
from news.models import News
from .models import Switcher, Profile
from meetings.models import Meeting, Apologies, Guests
from meetings.forms import apologies_form
from datetime import datetime
from datetime import date
from blog.models import Post
from django.template.context_processors import csrf
from machina.apps.forum_conversation.models import Post as Posting
from django.views.generic import TemplateView


def index(request):

    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,
                                     password=password)

            if user is not None:
                auth.login(request=request, user=user)
                messages.error(request, "You have successfully logged in")
                return redirect(reverse('switcher'))
            else:

                messages.error(request, "oops")
                messages.error(request, user)
                # redirects to switcher instead of dash to set group and business

    else:
        login_form = UserLoginForm()

    return render(request, 'index.html', {'login_form': login_form})



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


@login_required
def registration(request):

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        telephone = request.POST.get("telephone", "default")
        image = request.FILES.get("profile_image")

        if registration_form.is_valid() and profile_form.is_valid():
            xe = registration_form.save()
            xe.profile.telephone = telephone
            xe.profile.profile_image = image
            xe.save()
            return redirect(reverse('new_business'))

    registration_form = UserRegistrationForm()
    profile_form = ProfileForm()
    return render(request, 'registration.html', {'registration_form': registration_form, 'profile_form': profile_form})


@login_required
def user_profile(request):
    """the users profile page"""
    instance = Profile.objects.get(pk=request.user.pk)
    if request.method == "POST":

        form = ProfileForm(request.POST, request.FILES, instance=instance)
        form.save()
        return redirect(reverse('dashboard'))
        messages.error(request, "Profile Updated")

    profile = ProfileForm(instance=instance)
    return render(request, 'profile.html', {'profile': profile, 'instance': instance})


@login_required
def dashboard(request):

    # current user
    user = request.user
    # get new articles for dash
    articles = News.objects.all().order_by('date').reverse()[0:3]
    # get list of groups and business for user
    switchData = Switcher.objects.filter(user=user)
    # work out next meeting
    # todays date
    today = date.today()
    # limits the search to one and model in date order by group
    group = request.session['group']
    # show the latest meeting
    meeting = Meeting.objects.filter(meeting_date__gte=today, group=group)[0:1]
    # show any meeting requests

    guests = Guests.objects.filter(
        user=user, meeting__meeting_date__gte=today)

    # returns nummber of group members

    member_count = Switcher.objects.filter(group=group).count()

    # get group members details

    members = Switcher.objects.filter(group=group)

    # get blog posts and tags
    blog = Post.objects.filter(status=1).order_by('-created_on')[0:3]

    tags = Post.objects.order_by('tag').distinct('tag')

    posts = Posting.objects.all().order_by('pk').reverse()[0:3]

    return render(request, 'dashboard.html', {'tags': tags,
                                              'posts': posts,
                                              'blog': blog,
                                              'guests': guests,
                                              'articles': articles,
                                              'switchData': switchData,
                                              'meeting': meeting,
                                              'today': today,
                                              'members': members,
                                              'member_count': member_count})


@login_required
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


@login_required
def switching(request, pk):
    # changes the group and business based on the switcher instance by updating session cookies
    # filters switcher table by instance
    switchdata = Switcher.objects.get(pk=pk)
    # sets  variables
    grp = switchdata.group.pk
    bp = switchdata.business_profile.pk
    # resets session cookies
    request.session['group'] = grp
    request.session['bussprof'] = bp
    return redirect(reverse('dashboard'))


@login_required
def switcher_add(request):
    if request.method == "POST":
        switch = switcher_form(request.POST)
        if switch.is_valid():
            switch.save(commit=True)
            messages.error(request, "business Added")
            return redirect(reverse('dashboard'))
    else:

        switch = switcher_form()
        return render(request, 'switch_add.html', {'switch': switch})


@login_required
def apologies(request, pk):
    user = request.user
    meeting = Meeting.objects.get(pk=pk)
    apologies = apologies_form().save(commit=False)
    apologies.user = user
    apologies.meeting = meeting
    apologies.save()
    messages.error(request, 'apologies added')

    return redirect(reverse('dashboard'))


def test(request):
    return render(request, 'user-dashboard.html')


class ServiceWorkerView(TemplateView):
    template_name = 'sw.js'
    content_type = 'application/javascript'
    name = 'sw.js'


def error(request):
    return render(request, 'error.html')

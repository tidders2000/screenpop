from django.shortcuts import render, redirect, reverse
from .models import BusinessProfile
from .forms import bp_model_form, tiny_model_form, add_business
from django.contrib.auth.decorators import login_required
from accounts.models import Switcher
from business.models import BusinessProfile
from django.contrib import messages


@login_required
def market(request):

    all_members = Switcher.objects.all
    if request.method == "POST":
        keyword = request.POST.get('keyword')
        location = request.POST.get('location')
        type = request.POST.get('type')
        all_members = Switcher.objects.filter(
            business_profile__business_name__icontains=keyword).filter(business_profile__location__icontains=location).filter(business_profile__business_type__icontains=type)

    return render(request, 'marketplace.html', {'all_members': all_members})


@login_required
def business_profile(request):

    pk = request.session['bussprof']

    profile = BusinessProfile.objects.filter(
        pk=pk)

    return render(request, 'businessprofile.html', {'profile': profile})


@login_required
def edit_profile(request, pk):
    data = BusinessProfile.objects.get(pk=pk)
    tpk = pk
    profile = bp_model_form(instance=data)
    prof = BusinessProfile.objects.get(pk=pk)
    if request.method == "POST":
        form = bp_model_form(request.POST, request.FILES, instance=prof)
        form.save()
        return redirect(reverse('business_profile'))
        messages.error(request, "Profile Updated")

    return render(request, 'edit_profile.html', {'profile': profile, 'tpk': tpk})


@login_required
def edit_profile_b(request, pk):
    data = BusinessProfile.objects.get(pk=pk)
    tiny = tiny_model_form(instance=data)
    if request.method == "POST":
        form = tiny_model_form(request.POST, request.FILES, instance=data)
        form.save()
        return redirect(reverse('business_profile'))
        messages.error(request, "Profile Updated")
    return render(request, 'edit_profile_b.html', {'tiny': tiny})


@login_required
def bp_view(request, pk):
    profile = BusinessProfile.objects.filter(
        pk=pk)
    return render(request, 'businessprofile.html', {'profile': profile})


@login_required
def new_business(request):
    form = add_business()
    if request.method == "POST":
        new_bus = add_business(request.POST)
        if new_bus.is_valid():
            new_bus.save(commit=True)
            messages.error(request, "business Added")
            return redirect(reverse('switcher_add'))
    else:

        form = add_business()
        return render(request, 'add_profile.html', {'form': form})

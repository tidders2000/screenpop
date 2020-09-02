from django.shortcuts import render, redirect, reverse
from .models import BusinessProfile
from .forms import bp_model_form
from accounts.models import Switcher
from django.contrib import messages


def market(request):

    all_members = Switcher.objects.all

    return render(request, 'marketplace.html', {'all_members': all_members})


def business_profile(request):

    pk = request.session['bussprof']

    profile = BusinessProfile.objects.filter(
        pk=pk)

    return render(request, 'businessprofile.html', {'profile': profile})


def edit_profile(request, pk):
    data = BusinessProfile.objects.get(pk=pk)

    profile = bp_model_form(instance=data)

    return render(request, 'edit_profile.html', {'profile': profile})


def bp_view(request, pk):
    profile = BusinessProfile.objects.filter(
        pk=pk)
    return render(request, 'businessprofile.html', {'profile': profile})


def new_business(request):
    if request.method == "POST":
        new_bus = bp_model_form(request.POST)
        if new_bus.is_valid():
            new_bus.save(commit=True)
            messages.error(request, "business Added")
            return redirect(reverse('switcher_add'))
    else:

        profile = bp_model_form()
        return render(request, 'edit_profile.html', {'profile': profile})

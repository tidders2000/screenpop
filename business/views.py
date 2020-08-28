from django.shortcuts import render
from .models import BusinessProfile
from .forms import bp_model_form


def market(request):

    return render(request, 'marketplace.html')


def business_profile(request):

    pk = request.session['bussprof']

    profile = BusinessProfile.objects.filter(
        pk=pk)

    return render(request, 'businessprofile.html', {'profile': profile})


def edit_profile(request, pk):
    data = BusinessProfile.objects.get(pk=pk)

    profile = bp_model_form(instance=data)

    return render(request, 'edit_profile.html', {'profile': profile})

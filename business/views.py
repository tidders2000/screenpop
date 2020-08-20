from django.shortcuts import render


def market(request):
    return render(request, 'marketplace.html')


def business_profile(request):
    return render(request, 'businessprofile.html')

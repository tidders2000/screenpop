

import csv
import io
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from business.models import BusinessProfile
from accounts.models import Switcher
from groups.models import Groups
from meetings.models import Meeting
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
# Create your views here.
# one parameter named request


@login_required
def meeting_upload(request):
    # declaring template
    template = "uploader.html"
    data = User.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Meeting.objects.update_or_create(
            meeting_date=column[0],
            group=Groups.objects.filter(pk=column[1]).first(),
            zoom_link=column[2],
            agenda_item1=column[3],
            agenda_item2=column[4],
            agenda_item3=column[5],
            start_time=column[6]
        )

    context = {}
    return render(request, template, context)

# Create your views here.


@login_required
def profile_upload(request):
    # declaring template
    template = "meetingUploader.html"
    data = User.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = User.objects.update_or_create(
            username=column[0],
            first_name=column[1],
            last_name=column[2],
            email=column[3],
            password=make_password(column[4])
        )
        bp = BusinessProfile.objects.update_or_create(
            user=User.objects.latest('pk'),
            business_name=column[5]
        )

        switch = Switcher.objects.update_or_create(
            user=User.objects.latest('pk'),
            business_profile=BusinessProfile.objects.latest('pk'),
            group=Groups.objects.filter(pk=column[6]).first()
        )
    context = {}
    return render(request, template, context)


@login_required
def switcher_upload(request):
    # declaring template
    template = "switcher_upload.html"
    data = User.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Switcher.objects.update_or_create(
            user=User.objects.filter(username=column[0]).first(),
            group=Groups.objects.filter(pk=column[1]).first(),

            business_profile=BusinessProfile.objects.filter(
                pk=column[2]).first()

        )

    context = {}
    return render(request, template, context)


@login_required
def business_upload(request):
    # declaring template
    template = "business_upload.html"
    data = User.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = BusinessProfile.objects.update_or_create(
            user=User.objects.filter(username=column[0]).first(),
            business_name=column[1]

        )

    context = {}
    return render(request, template, context)


@login_required
def bulk_email(request):
    # declaring template
    template = "bulk_email.html"
    data = User.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email, address,    phone, profile',
        'profiles': data
    }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')

    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        send_mail(
            subject="ScreenPop App",
            message='Dear ' +
            column[0] + '\n \n Please find your logon details for the new ScreenPop App. You are part of the test group and I would be grateful if you could flag up any issues or bugs to me at simon@scruffyhorse.com '
            + ' \n \n Please use your email and the following password ' +
            column[1] + ' and you can logon at:\n\n ' + column[3] +
            '\n \n If you would like some help on getting the most out of the app click the ? (Help) in the top right corner after you have logged on. \n\n Best Wishes Simon',

            from_email='simon@scruffyhorse.com',
            recipient_list=[column[2]],

            fail_silently=False)

    context = {}
    return render(request, template, context)

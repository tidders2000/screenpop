from django.db import models
from django.db.models.fields import EmailField
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from groups.models import Groups
from business.models import BusinessProfile
from django.contrib.postgres.fields import ArrayField

from datetime import datetime

status = [('Pending', 'Pending'),
          ('Declined', 'Declined'), ('Approved', 'Approved')]


class Meeting(models.Model):

    meeting_date = models.DateField()
    group = models.ForeignKey(Groups, null=True, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=10, default='start time')
    zoom_link = models.URLField(blank=True)
    presenter = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Notes = models.CharField(max_length=254, default='Agenda Item')
    agenda_item2 = models.CharField(max_length=254, default='Agenda Item')
    agenda_item3 = models.CharField(max_length=254, default='Agenda Item')

    class Meta:
        ordering = ['meeting_date']

    def __str__(self):
        return 'date {} group {} id{}'.format(self.meeting_date, self.group, self.pk)


class Visitors(models.Model):
    
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    email = EmailField(default="user@user.com")
    business =   models.CharField(max_length=60)
    meeting = models.ForeignKey(Meeting, null=True, on_delete=models.CASCADE)
    website =   models.CharField(max_length=60)
 
    def __str__(self):
        return 'first_name:{},second_name:{}, business{}'.format(self.first_name, self.second_name,self.business)


class Guests(models.Model):
    meeting = models.ForeignKey(Meeting, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    business =  models.ForeignKey(BusinessProfile, null=True, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=254, choices=status, default='pending')

    def __str__(self):
        return 'name:{},meeting{}'.format(self.user, self.meeting)


class Apologies(models.Model):
    meeting = models.ForeignKey(Meeting, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Hosts(models.Model):
     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
     group = models.ForeignKey(Groups, null=True, on_delete=models.CASCADE)

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from groups.models import Groups

from datetime import datetime

status = [('Pending', 'Pending'),
          ('Declined', 'Declined'), ('Approved', 'Approved')]


class Meeting(models.Model):

    meeting_date = models.DateField()
    group = models.ForeignKey(Groups, null=True, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=10, default='start time')
    zoom_link = models.URLField(blank=True)
    agenda_item1 = models.CharField(max_length=254, default='Agenda Item')
    agenda_item2 = models.CharField(max_length=254, default='Agenda Item')
    agenda_item3 = models.CharField(max_length=254, default='Agenda Item')

    class Meta:
        ordering = ['meeting_date']

    def __str__(self):
        return 'date {} group {} id{}'.format(self.meeting_date, self.group, self.pk)


class Visitors(models.Model):
    name = models.CharField(max_length=254, default='name')
    business = models.CharField(max_length=254, default='business')
    meeting = models.ForeignKey(Meeting, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'name:{}, business{}'.format(self.name, self.business)


class Guests(models.Model):
    meeting = models.ForeignKey(Meeting, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=254, choices=status, default='pending')

    def __str__(self):
        return 'name:{},meeting{}'.format(self.user, self.meeting)


class Apologies(models.Model):
    meeting = models.ForeignKey(Meeting, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.


class Groups(models.Model):
    groupName = models.CharField(max_length=254, default=0)
    groupLocation = models.CharField(max_length=254, default=0)
    created = models.DateField(auto_now_add=True)
    about = HTMLField()
   
    image = models.ImageField(upload_to='media/images')

    def __str__(self):
        return self.groupName

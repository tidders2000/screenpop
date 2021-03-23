from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class News(models.Model):

    headline = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='media/images')
    article = HTMLField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.headline

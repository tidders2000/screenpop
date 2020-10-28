from django.db import models
from tinymce.models import HTMLField
from phone_field import PhoneField
from django.contrib.auth.models import User
from groups.models import Groups

businessTypes = [('Graphic Design', 'Graphic Design'),
                 ('Accountant', 'Accountant'), ('Solicitor', 'Solicitor'), ('Default', 'Default')]

legalEntity = [('Sole trader', 'Sole trader'), ('Partnership',
                                                'Partnership'), ('Limited Company', 'Limited Company')]

# Create your models here.


class BusinessProfile(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=254, blank=False)

    e_mail = models.EmailField(max_length=150, default='name@somewhere.com')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    business_type = models.CharField(
        max_length=254, choices=businessTypes, default='Default')
    logo = models.ImageField(upload_to='media/images',
                             blank=True, default='media/images/default_1.png')
    opening_hours = models.CharField(max_length=254, default='09:00-17:00')
    number_emp = models.IntegerField(default=0)
    location = models.CharField(max_length=254, default='Bristol, UK')
    country = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    street_address1 = models.CharField(max_length=40, blank=True)
    street_address2 = models.CharField(max_length=40, blank=True)
    county = models.CharField(max_length=40, blank=True)
    contact_name = models.CharField(max_length=254, default="My Name")
    about = HTMLField(blank=True)
    services = HTMLField(blank=True)
    website = models.CharField(max_length=254, default='https://example.com')
    header_image = models.ImageField(
        upload_to='media/images', blank=True, default='media/images/header_1.jpg')
    facebook = models.CharField(max_length=254, default='https://example.com')
    linkedin = models.CharField(max_length=254, default='https://example.com')
    google = models.CharField(max_length=254, default='https://example.com')
    twitter = models.CharField(max_length=254, default='https://example.com')
    legal_entity = models.CharField(
        max_length=254, choices=legalEntity, default='Sole trader')

    def __str__(self):
        return self.business_name

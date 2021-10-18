from django.db import models
from tinymce.models import HTMLField
from phone_field import PhoneField
from django.contrib.auth.models import User
from groups.models import Groups

businessTypes = [('Graphic Design', 'Graphic Design'),
                 ('Accountant', 'Accountant'),
                 ('App Designer', 'App Designer'),

                 ('Default', 'Default'),
                 ('Business Consultant',
                  'Business Consultant'),
                 ('Business Support', 'Business Support'),
                 ('Charity', 'Charity'),
                 ('SEO', 'SEO'),
                 ('Web Design', 'Web Design'),
                 ('Beauty products', 'Beauty products'),
                 ('BookKeeper', 'BookKeeper'),
                 ('Business Coach', 'Business Coach'),
                 ('Charity', 'Charity'),
                 ('Cake Maker', 'Cake Maker'),
                 ('Cleaning', 'Cleaning'),
                 ('Food', 'Food'),
                 ('Financial Consultant', 'Financial Consultant'),
                 ('Health & Safety', 'Health & Safety'),
                 ('Cards & Gifts', 'Cards&Gifts'),
                 ('Health Coach', 'Health Coach'),
                 ('Health', 'Health'),
                 ('HR', 'HR'),
                 ('IT Support', 'IT Support'),
                 ('Life Coach', 'Life Coach'),
                 ('Mortgage Advisor', 'Mortgage Advisor'),
                 ('Marketing', 'Marketing'),
                 ('Nutritional Products', 'Nutritional Products'),
                 ('Personal Trainer', 'Personal Trainer'),
                 ('Photographer', 'Photographer'),
                 ('Physio', 'Physio'),
                 ('Psychologist', 'Psychologist'),
                 ('Social Media', 'Social Media'),
                 ('Software', 'Software'),
                 ('Solicitor', 'Solicitor'),
                 ('Stylist', 'Stylist'),
                 ('Teaching', 'Teaching'),
                 ('Therapist', 'Therapist'),
                 ('Travel', 'Travel'),
                 ('Utilities Provider', 'Utilities Provider'),
                 ('Virtual Assistant', 'Virtual Assistant'),
                 ('Will Writer', 'Will Writer')






                 ]


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
    instagram = models.CharField(max_length=254, default='https://example.com')
    legal_entity = models.CharField(
        max_length=254, choices=legalEntity, default='Sole trader')
    class Meta:
        ordering = ('business_name',)
    def __str__(self):
        return self.business_name

# Generated by Django 3.1 on 2020-11-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0023_auto_20201028_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='business_type',
            field=models.CharField(choices=[('Graphic Design', 'Graphic Design'), ('Accountant', 'Accountant'), ('App Designer', 'App Designer'), ('Default', 'Default'), ('Business Consultant', 'Business Consultant'), ('Business Support', 'Business Support'), ('SEO', 'SEO'), ('Web Design', 'Web Design'), ('Beauty products', 'Beauty products'), ('BookKeeper', 'BookKeeper'), ('Business Coach', 'Business Coach'), ('Charity', 'Charity'), ('Cake Maker', 'Cake Maker'), ('Cleaning', 'Cleaning'), ('Food', 'Food'), ('Financial Consultant', 'Financial Consultant'), ('Health & Safety', 'Health & Safety'), ('Cards & Gifts', 'Cards&Gifts'), ('Health Coach', 'Health Coach'), ('Health', 'Health'), ('HR', 'HR'), ('IT Support', 'IT Support'), ('Life Coach', 'Life Coach'), ('Mortgage Advisor', 'Mortgage Advisor'), ('Marketing', 'Marketing'), ('Nutritional Products', 'Nutritional Products'), ('Personal Trainer', 'Personal Trainer'), ('Photographer', 'Photographer'), ('Physio', 'Physio'), ('Psychologist', 'Psychologist'), ('Social Media', 'Social Media'), ('Software', 'Software'), ('Solicitor', 'Solicitor'), ('Stylist', 'Stylist'), ('Teaching', 'Teaching'), ('Therapist', 'Therapist'), ('Travel', 'Travel'), ('Utilities Provider', 'Utilities Provider'), ('Virtual Assistant', 'Virtual Assistant'), ('Will Writer', 'Will Writer')], default='Default', max_length=254),
        ),
    ]

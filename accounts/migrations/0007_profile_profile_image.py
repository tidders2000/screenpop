# Generated by Django 3.1 on 2020-08-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_switcher'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='media/profiles'),
        ),
    ]

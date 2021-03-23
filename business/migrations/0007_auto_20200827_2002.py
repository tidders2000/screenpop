# Generated by Django 3.1 on 2020-08-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_remove_businessprofile_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='business_name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='country',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='county',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='facebook',
            field=models.CharField(default='enter a link', max_length=254),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='location',
            field=models.CharField(default='Bristol, UK', max_length=254),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='number_emp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='opening_hours',
            field=models.CharField(default='09:00-17:00', max_length=254),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='street_address2',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='town_or_city',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]

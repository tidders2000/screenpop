# Generated by Django 3.1 on 2020-08-24 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='image',
            field=models.ImageField(default=1, upload_to='media/images'),
            preserve_default=False,
        ),
    ]

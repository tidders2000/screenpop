# Generated by Django 3.1 on 2020-09-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0012_auto_20200927_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='logo',
            field=models.ImageField(default='member-3.png', upload_to='media/images'),
        ),
    ]

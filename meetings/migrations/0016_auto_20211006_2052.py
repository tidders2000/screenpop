# Generated by Django 3.1.3 on 2021-10-06 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0015_auto_20210927_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='presenter',
            field=models.CharField(max_length=254, null=True),
        ),
    ]

# Generated by Django 3.1 on 2020-08-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0009_auto_20200827_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessprofile',
            name='website',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]

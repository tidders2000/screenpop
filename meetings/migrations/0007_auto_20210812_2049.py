# Generated by Django 3.1.3 on 2021-08-12 20:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_guests_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='business',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), default=['{business}'], size=None),
        ),
    ]
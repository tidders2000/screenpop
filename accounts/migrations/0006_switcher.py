# Generated by Django 3.1 on 2020-08-27 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_remove_businessprofile_group'),
        ('groups', '0002_groups_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20200815_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='switcher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.businessprofile')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET, to='groups.groups')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
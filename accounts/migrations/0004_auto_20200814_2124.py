# Generated by Django 3.1 on 2020-08-14 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20200814_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='BusinessName',
        ),
        migrations.AddField(
            model_name='profile',
            name='businessname',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]

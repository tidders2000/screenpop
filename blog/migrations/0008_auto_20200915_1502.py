# Generated by Django 3.1 on 2020-09-15 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200915_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tag'),
        ),
    ]

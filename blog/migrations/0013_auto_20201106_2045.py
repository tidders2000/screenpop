# Generated by Django 3.1 on 2020-11-06 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200924_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Digital', 'Digital'), ('StartUp', 'StartUp'), ('Finance', 'Finance'), ('Marketing', 'Marketing'), ('HR', 'HR'), ('Legal', 'Legal'), ('Web', 'Web'), ('Social Media', 'Social Media'), ('Fitness', 'Fitness'), ('Wellbeing', 'Wellbeing'), ('Gifts', 'Gifts'), ('Homemade', 'Homemade'), ('Support', 'Support'), ('Training', 'Training'), ('Advice', 'Advice'), ('Advertising', 'Advertising'), ('Coaching', 'Coaching'), ('Help', 'Help'), ('Money Saving', 'Money Saving')], max_length=200),
        ),
    ]

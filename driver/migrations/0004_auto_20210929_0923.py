# Generated by Django 3.2.7 on 2021-09-29 03:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_rename_driverid_drivertrip_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivertrip',
            name='Vehicle_Name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='drivertrip',
            name='Vehicle_Number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Vehicle number must be entered in the format.', regex='^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$')]),
        ),
    ]

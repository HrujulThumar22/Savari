# Generated by Django 3.2.7 on 2021-10-28 09:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0006_auto_20211005_0847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drivertrip',
            name='Trip_Ending_Date',
        ),
        migrations.RemoveField(
            model_name='drivertrip',
            name='Trip_Ending_Time',
        ),
        migrations.RemoveField(
            model_name='drivertrip',
            name='Trip_Starting_Date',
        ),
        migrations.RemoveField(
            model_name='drivertrip',
            name='Trip_Starting_Time',
        ),
        migrations.AddField(
            model_name='drivertrip',
            name='Trip_Created_On',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
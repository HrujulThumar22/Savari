# Generated by Django 3.2.7 on 2021-10-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passengerTrip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertrip',
            name='isTripComfirmed',
        ),
        migrations.AddField(
            model_name='usertrip',
            name='requestStatus',
            field=models.CharField(choices=[('0', 'Unattended'), ('1', 'Accepted'), ('2', 'Rejected')], default=0, max_length=1),
        ),
    ]

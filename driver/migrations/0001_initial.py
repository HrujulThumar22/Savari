# Generated by Django 3.2.7 on 2021-09-22 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0002_auto_20210922_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trip_Starting_Date', models.DateField()),
                ('Trip_Starting_Time', models.TimeField()),
                ('Trip_Ending_Date', models.DateField()),
                ('Trip_Ending_Time', models.TimeField()),
                ('isTripStarted', models.BooleanField(default=False)),
                ('Destination_City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_city', to='city.city')),
                ('Starting_City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_city', to='city.city')),
            ],
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0008_auto_20211028_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivertrip',
            name='profilepic',
            field=models.ImageField(default='image.jpg', upload_to='vimages/'),
        ),
    ]

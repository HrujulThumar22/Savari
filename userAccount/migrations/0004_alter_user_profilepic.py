# Generated by Django 3.2.7 on 2021-10-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAccount', '0003_alter_user_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilepic',
            field=models.ImageField(default='image.jpg', upload_to='images/'),
        ),
    ]

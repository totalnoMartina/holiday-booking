# Generated by Django 3.2 on 2022-03-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0002_guest_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='description',
        ),
        migrations.AddField(
            model_name='apartment',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

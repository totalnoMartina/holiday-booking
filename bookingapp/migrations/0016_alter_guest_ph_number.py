# Generated by Django 3.2 on 2022-04-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0015_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='ph_number',
            field=models.CharField(max_length=40),
        ),
    ]
# Generated by Django 2.2.7 on 2019-11-12 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognize', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='date_of_registration',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='students',
            name='date_of_registration',
            field=models.DateField(),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_registration_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='address',
            field=models.JSONField(null=True),
        ),
    ]

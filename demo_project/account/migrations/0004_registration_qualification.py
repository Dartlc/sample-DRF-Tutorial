# Generated by Django 3.1.3 on 2020-11-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_registration_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='qualification',
            field=models.JSONField(null=True),
        ),
    ]
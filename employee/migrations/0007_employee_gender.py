# Generated by Django 5.0.4 on 2024-04-26 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_addressinformation_address_line_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]

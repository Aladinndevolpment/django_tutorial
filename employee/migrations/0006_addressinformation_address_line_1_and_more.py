# Generated by Django 5.0.4 on 2024-04-26 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_employee_addressinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressinformation',
            name='address_line_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='addressinformation',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='addressinformation',
            name='pin_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='addressinformation',
            name='state',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
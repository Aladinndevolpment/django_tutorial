# Generated by Django 5.0.4 on 2024-04-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=3),
        ),
    ]

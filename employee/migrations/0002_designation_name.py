# Generated by Django 5.0.4 on 2024-04-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designation',
            name='name',
            field=models.CharField(default='Developer', max_length=30, unique=True),
        ),
    ]

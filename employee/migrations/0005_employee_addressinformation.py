# Generated by Django 5.0.4 on 2024-04-26 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30, unique=True)),
                ('last_name', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('contact', models.CharField(max_length=15, unique=True)),
                ('password', models.TextField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='employee/')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee', to='employee.designation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AddressInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('address', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='employee.employee')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-24 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_designation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='employee/'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employee', to='employee.designation'),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-26 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_employee_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='O', max_length=1),
        ),
    ]

# Generated by Django 3.2 on 2021-04-26 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_rename_emplpyeestatistics_employeestatistics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationinformation',
            name='id',
        ),
        migrations.AlterField(
            model_name='organizationinformation',
            name='emplpyee_statistics',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='survey.employeestatistics'),
        ),
    ]

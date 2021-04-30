# Generated by Django 3.2 on 2021-04-26 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmplpyeeStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trained_employee_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_description', models.CharField(max_length=500)),
                ('emplpyee_statistics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.emplpyeestatistics')),
            ],
        ),
    ]
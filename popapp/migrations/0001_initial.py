# Generated by Django 4.2.5 on 2023-09-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TicketNumber', models.IntegerField()),
                ('Customer', models.CharField(max_length=100)),
                ('CustomerAddress', models.CharField(max_length=200)),
                ('CustomerContactNumber', models.IntegerField()),
                ('DateOfService', models.DateField()),
                ('TechnicianName', models.CharField(max_length=100)),
                ('JobDescription', models.TextField()),
            ],
        ),
    ]
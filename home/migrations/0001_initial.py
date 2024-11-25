# Generated by Django 5.1.3 on 2024-11-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GmServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_name', models.CharField(max_length=100)),
                ('services_period', models.IntegerField()),
                ('services_fess', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NewService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]

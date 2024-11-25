# Generated by Django 5.1.3 on 2024-11-25 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('adhar', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=30)),
                ('avatar', models.ImageField(upload_to='avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Family_lead', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Mukhiya', to='home.person')),
                ('members', models.ManyToManyField(related_name='families', to='home.person')),
            ],
        ),
    ]

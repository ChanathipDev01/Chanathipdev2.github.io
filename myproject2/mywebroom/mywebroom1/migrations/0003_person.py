# Generated by Django 4.2.10 on 2024-03-15 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebroom1', '0002_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=500)),
            ],
        ),
    ]

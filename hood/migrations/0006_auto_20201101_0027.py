# Generated by Django 3.1.2 on 2020-10-31 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_emergencyservice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emergencyservice',
            options={'ordering': ['create_at']},
        ),
    ]

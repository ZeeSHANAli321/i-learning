# Generated by Django 4.2.4 on 2023-09-23 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_contact_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='about',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='price',
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-23 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_batch_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='price',
            field=models.IntegerField(default='000'),
        ),
    ]

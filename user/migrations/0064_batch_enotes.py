# Generated by Django 4.2.4 on 2023-09-27 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0063_enotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='eNotes',
            field=models.ManyToManyField(blank=True, to='user.enotes'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0062_batch_assignments'),
    ]

    operations = [
        migrations.CreateModel(
            name='eNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='student/batches/Notes')),
            ],
        ),
    ]

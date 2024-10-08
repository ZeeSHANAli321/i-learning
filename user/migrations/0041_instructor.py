# Generated by Django 4.2.4 on 2023-09-24 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0040_alter_batch_previewvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('image', models.ImageField(upload_to='instructor/images')),
                ('about', models.TextField()),
                ('qualifications', models.CharField(max_length=500)),
                ('technologies', models.TextField()),
                ('channel', models.URLField(null=True)),
            ],
        ),
    ]

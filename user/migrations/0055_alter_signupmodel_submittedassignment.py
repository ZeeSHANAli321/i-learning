# Generated by Django 4.2.4 on 2023-09-26 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0054_signupmodel_submittedassignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='submittedAssignment',
            field=models.ManyToManyField(default=FileNotFoundError, to='user.sbmtassignment'),
        ),
    ]

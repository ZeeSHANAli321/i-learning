# Generated by Django 4.2.4 on 2023-09-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_sbmtassignment_assignment_file_and_more'),
        ('user', '0058_alter_signupmodel_submittedassignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupmodel',
            name='submittedAssignment',
            field=models.ManyToManyField(blank=True, to='student.sbmtassignment'),
        ),
    ]
# Generated by Django 4.1.13 on 2025-03-24 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_MSSQLdb_App', '0005_courses_tracks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainers',
            old_name='trainer_firstname',
            new_name='trainer_name',
        ),
        migrations.RemoveField(
            model_name='trainers',
            name='trainer_lastname',
        ),
        migrations.AddField(
            model_name='students_info',
            name='student_city',
            field=models.CharField(default='x', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students_info',
            name='student_country',
            field=models.CharField(default='s', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students_info',
            name='student_state',
            field=models.CharField(default='ser', max_length=100),
            preserve_default=False,
        ),
    ]

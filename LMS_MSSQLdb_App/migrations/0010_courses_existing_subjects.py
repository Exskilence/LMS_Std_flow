# Generated by Django 4.1.13 on 2025-04-03 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_MSSQLdb_App', '0009_alter_admins_reg_date_alter_courses_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='Existing_Subjects',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

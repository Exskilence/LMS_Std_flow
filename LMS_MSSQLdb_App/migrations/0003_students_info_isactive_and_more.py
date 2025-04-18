# Generated by Django 4.1.13 on 2025-03-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_MSSQLdb_App', '0002_course_plan_details_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_info',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='students_info',
            name='student_alt_phone',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students_info',
            name='student_dob',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='students_info',
            name='student_pincode',
            field=models.CharField(default=12, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students_info',
            name='student_qualification',
            field=models.CharField(default='xtz', max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.13 on 2025-03-27 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS_MSSQLdb_App', '0008_admins_alter_questions_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='reg_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='modified_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='creation_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='last_updated_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sub_topics',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sub_topics',
            name='modified_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='modified_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='topics',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='topics',
            name='modified_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tracks',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tracks',
            name='modified_at',
            field=models.DateTimeField(),
        ),
    ]

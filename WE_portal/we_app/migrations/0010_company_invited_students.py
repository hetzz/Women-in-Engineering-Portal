# Generated by Django 2.2.2 on 2019-06-26 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('we_app', '0009_student_profile_faculty_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='invited_students',
            field=models.CharField(default='', max_length=100),
        ),
    ]

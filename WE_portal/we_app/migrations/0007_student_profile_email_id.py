# Generated by Django 2.2.2 on 2019-06-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('we_app', '0006_student_profile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_profile',
            name='email_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
# Generated by Django 2.2.2 on 2019-06-26 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('we_app', '0011_auto_20190626_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(default='Faculty', max_length=150)),
                ('faculty_email_id', models.CharField(max_length=100)),
                ('full_name', models.CharField(default='Student', max_length=100)),
                ('email_id', models.CharField(default='NA', max_length=100)),
                ('faculty_review', models.CharField(default='Good', max_length=1000)),
                ('faculty_points', models.IntegerField(default=50)),
                ('faculty_grade', models.CharField(default='C', max_length=10)),
            ],
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('we_app', '0010_company_invited_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(default='Company', max_length=150)),
                ('invited_students', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='invited_students',
        ),
    ]
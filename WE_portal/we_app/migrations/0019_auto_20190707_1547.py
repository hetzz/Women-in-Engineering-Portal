# Generated by Django 2.2.2 on 2019-07-07 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('we_app', '0018_auto_20190702_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_email_id', models.CharField(max_length=100)),
                ('csv', models.FileField(blank=True, null=True, upload_to='CSV/<django.db.models.fields.CharField>')),
            ],
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='Resume'),
        ),
    ]

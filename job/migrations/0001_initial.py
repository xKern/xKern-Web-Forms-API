# Generated by Django 3.1.3 on 2020-11-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('job', models.CharField(max_length=100)),
                ('resume', models.FileField(max_length=1024, upload_to='./uploads/resumes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Job applications',
                'ordering': ['created_at'],
            },
        ),
    ]
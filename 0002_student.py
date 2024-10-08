# Generated by Django 5.1 on 2024-08-08 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_rollno', models.IntegerField()),
                ('student_name', models.CharField(max_length=50)),
                ('student_age', models.IntegerField()),
                ('student_email', models.CharField(max_length=50)),
                ('student_subject', models.CharField(choices=[('science', 'science'), ('arts', 'arts'), ('commerce', 'commerce')], max_length=50)),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-11-03 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_rename_student_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Student',
        ),
    ]

# Generated by Django 4.2 on 2023-05-06 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='exam',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='student',
        ),
    ]

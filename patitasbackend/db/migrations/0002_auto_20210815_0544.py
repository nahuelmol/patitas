# Generated by Django 3.2 on 2021-08-15 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
    ]

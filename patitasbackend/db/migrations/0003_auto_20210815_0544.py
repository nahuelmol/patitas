# Generated by Django 3.2 on 2021-08-15 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20210815_0544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='published',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-31 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20181028_1213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]

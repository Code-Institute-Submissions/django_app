# Generated by Django 2.1.7 on 2019-04-01 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bugs',
            old_name='created_date',
            new_name='published_date',
        ),
    ]

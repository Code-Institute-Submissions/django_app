# Generated by Django 2.1.7 on 2019-04-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0003_auto_20190406_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Waiting'), ('In progress', 'In progress'), ('Completed', 'Completed')], default=('Waiting', 'Waiting'), max_length=50),
        ),
    ]

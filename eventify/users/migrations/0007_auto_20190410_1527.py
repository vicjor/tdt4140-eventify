# Generated by Django 2.1.5 on 2019-04-10 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_merge_20190409_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='link',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='read',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='sender',
        ),
    ]
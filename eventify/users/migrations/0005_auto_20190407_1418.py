# Generated by Django 2.1.5 on 2019-04-07 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190407_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='on_contact',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='on_event_host',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='on_event_invite',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='on_event_update_delete',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-08 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='desc',
            new_name='description',
        ),
    ]

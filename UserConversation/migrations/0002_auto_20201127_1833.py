# Generated by Django 3.0.8 on 2020-11-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserConversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessages',
            name='messageReadTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='messageReceivedTime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

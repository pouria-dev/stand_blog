# Generated by Django 5.1.1 on 2024-10-02 00:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_alter_message_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 2, 0, 36, 54, 79996, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 2.2 on 2021-05-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtags', '0006_auto_20210112_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='has_audio',
            field=models.BooleanField(default=False),
        ),
    ]

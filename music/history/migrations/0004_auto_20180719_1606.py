# Generated by Django 2.0.7 on 2018-07-19 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_auto_20180719_1602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist_id',
            new_name='artist',
        ),
    ]
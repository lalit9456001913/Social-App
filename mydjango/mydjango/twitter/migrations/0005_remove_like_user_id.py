# Generated by Django 3.0.2 on 2020-01-07 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_remove_like_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='user_id',
        ),
    ]

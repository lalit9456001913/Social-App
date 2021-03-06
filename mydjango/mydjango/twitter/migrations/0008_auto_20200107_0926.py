# Generated by Django 3.0.2 on 2020-01-07 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter', '0007_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dislike',
            name='post_id',
        ),
        migrations.AddField(
            model_name='dislike',
            name='post_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='twitter.Post'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='dislike',
            name='user_id',
        ),
        migrations.AddField(
            model_name='dislike',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

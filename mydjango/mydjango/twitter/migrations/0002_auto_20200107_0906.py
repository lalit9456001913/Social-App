# Generated by Django 3.0.2 on 2020-01-07 09:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('dislike_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.ManyToManyField(to='twitter.Post')),
                ('user_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

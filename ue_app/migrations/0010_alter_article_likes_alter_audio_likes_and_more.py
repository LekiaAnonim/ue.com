# Generated by Django 4.1.4 on 2023-01-18 02:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ue_app', '0009_remove_article_like_remove_audio_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='ue_app_article_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='audio',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='ue_app_audio_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='ue_app_video_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
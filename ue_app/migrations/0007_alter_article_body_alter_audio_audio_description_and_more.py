# Generated by Django 4.1.4 on 2023-01-14 21:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ue_app', '0006_article_tags_audio_tags_video_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='audio_description',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_description',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]

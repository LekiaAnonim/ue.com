# Generated by Django 4.1.4 on 2023-01-14 22:53

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ue_app', '0007_alter_article_body_alter_audio_audio_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='feature_image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='audio_upload',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Audio'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='feature_image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_upload',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, null=True, verbose_name='Video'),
        ),
    ]
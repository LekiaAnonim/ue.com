# Generated by Django 4.1.4 on 2023-01-06 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ue_app', '0003_alter_video_video_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_image'),
        ),
        migrations.AddField(
            model_name='channel',
            name='display_name',
            field=models.CharField(blank=True, help_text='Enter the name of your channel', max_length=200, null=True),
        ),
    ]

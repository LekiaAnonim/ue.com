# Generated by Django 4.1.4 on 2023-01-05 22:34

from django.db import migrations, models
import ue_app.models.video_model


class Migration(migrations.Migration):

    dependencies = [
        ('ue_app', '0002_alter_audio_audio_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_upload',
            field=models.FileField(upload_to=ue_app.models.video_model.user_directory_path),
        ),
    ]
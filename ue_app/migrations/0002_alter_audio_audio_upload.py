# Generated by Django 4.1.4 on 2023-01-05 22:34

from django.db import migrations, models
import ue_app.models.audio_model


class Migration(migrations.Migration):

    dependencies = [
        ('ue_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_upload',
            field=models.FileField(upload_to=ue_app.models.audio_model.user_directory_path),
        ),
    ]

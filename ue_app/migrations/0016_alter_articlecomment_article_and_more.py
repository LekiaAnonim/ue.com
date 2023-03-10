# Generated by Django 4.1.4 on 2023-03-04 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ue_app', '0015_remove_articlecomment_channel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ue_app.article'),
        ),
        migrations.AlterField(
            model_name='articlecomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ue_app.articlecomment'),
        ),
        migrations.AlterField(
            model_name='audiocomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ue_app.audiocomment'),
        ),
        migrations.AlterField(
            model_name='videocomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ue_app.videocomment'),
        ),
    ]

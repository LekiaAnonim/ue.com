# Generated by Django 4.1.4 on 2023-01-19 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ue_app', '0010_alter_article_likes_alter_audio_likes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='bio',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='address',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='city',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='country',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='email_confirmed',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='region',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='user',
        ),
        migrations.AddField(
            model_name='channel',
            name='banner',
            field=models.ImageField(blank=True, default='banner.png', null=True, upload_to='channel_banner'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, help_text='Enter your middle name', max_length=200, null=True)),
                ('photo', models.ImageField(blank=True, default='avatar.png', null=True, upload_to='profile_picture')),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(help_text='Enter your State or Phone Number', max_length=12, null=True)),
                ('address', models.CharField(blank=True, help_text='Enter your House address', max_length=500, null=True)),
                ('city', models.CharField(blank=True, help_text='Enter your City (e.g. Lagos)', max_length=100, null=True)),
                ('region', models.CharField(blank=True, help_text='Enter your State or Region (e.g. Rivers)', max_length=100, null=True)),
                ('country', models.CharField(blank=True, help_text='Enter your Country (e.g. Nigeria)', max_length=100, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel', to='ue_app.profile'),
        ),
    ]

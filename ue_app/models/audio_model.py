from ue_app.models.article_model import MediumInfo
from ue_app.validators import validate_is_audio
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from filebrowser.fields import FileBrowseField
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}_{3}'.format(instance.author.id, filename, "audios", instance.id)


class Audio(MediumInfo):
    feature_image = models.ImageField(null=True, blank=True,
                                      default='audio_image', upload_to="audio_images")

    audio_description = tinymce_models.HTMLField(null=True)
    audio_upload = models.FileField(null=True, upload_to=user_directory_path)

    likes = models.ManyToManyField(
        User, blank=True, related_name='ue_app_audio_likes')

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def already_liked(self):
        user = self.author.profile.user
        if user.is_authenticated:
            if user in self.likes.all():
                liked = True
            else:
                liked = False
            return liked

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('ue_app:audio_detail', kwargs={'username': self.author.display_name.lower(), 'slug': self.slug})

    def get_like_url(self):
        return reverse('ue_app:audio_like_toggle', kwargs={'username': self.author.display_name.lower(), 'slug': self.slug})

    def get_api_like_url(self):
        return reverse('ue_app:audio_api_like_toggle', kwargs={'username': self.author.display_name.lower(), 'slug': self.slug})

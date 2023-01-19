from ue_app.models.article_model import MediumInfo
from ue_app.validators import validate_is_video
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
# from filebrowser.fields import FileBrowseField

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}_{3}'.format(instance.author.id, filename, "videos", instance.slug)


class Video(MediumInfo):
    video_description = tinymce_models.HTMLField(null=True)
    video_upload = models.FileField(
        # upload_to=user_directory_path, validators=(validate_is_video,))
        upload_to=user_directory_path, null=True)
    # models.FileField(
    #     # upload_to=user_directory_path, validators=(validate_is_video,))
    #     upload_to=user_directory_path)

    likes = models.ManyToManyField(
        User, blank=True, related_name='ue_app_video_likes')

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
        return reverse('ue_app:video_detail', kwargs={'username': self.author.display_name.lower(), 'slug': self.slug})

    def get_like_url(self):
        return reverse('ue_app:video_like_toggle', kwargs={'username': self.author.display_name.lower(), 'slug': self.slug})

    def get_api_like_url(self):
        return reverse('ue_app:video_api_like_toggle', kwargs={'username': self.author.display_name.lower(), 'slug': self.slug})

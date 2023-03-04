from django.db import models
from ue_app.models.channel_model import Channel
from ue_app.models.article_model import Article
from ue_app.models.video_model import Video
from ue_app.models.audio_model import Audio
from django.utils import timezone
from django.contrib.auth.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(help_text="Enter your comment", null=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.comment}"


class ArticleComment(Comment):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Article Comment"



class VideoComment(Comment):
    video = models.ForeignKey(
        Video, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Video Comment"


class AudioComment(Comment):
    audio = models.ForeignKey(
        Audio, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Audio Comment"



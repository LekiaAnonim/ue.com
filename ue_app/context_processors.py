from django.conf import settings
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from ue_app.models.channel_model import Channel
from ue_app.models.article_model import MediumInfo, Article
from ue_app.models.audio_model import Audio
from ue_app.models.category_model import Category
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from ue_app.models.video_model import Video

from ue_app.forms.authentication.registration_form import UserRegisterForm
from django.contrib import messages
from django.db.models import Count

def base_data(request):
    data = {}
    data["register_form"] = UserRegisterForm()
    articles = Article.objects.annotate(likes_count=Count('likes')).order_by('-date_uploaded', '-likes_count', '-views')
    audios = Audio.objects.annotate(likes_count=Count('likes')).order_by('-date_uploaded', '-likes_count', '-views')
    videos = Video.objects.annotate(likes_count=Count('likes')).order_by('-date_uploaded', '-likes_count', '-views')
    recommended_articles = Article.objects.filter(author__follow = request.user.id).annotate(likes_count=Count('likes')).order_by('-date_uploaded', '-likes_count', '-views')
    recommended_audios = Audio.objects.filter(author__follow = request.user.id).annotate(likes_count=Count('likes')).order_by('-date_uploaded', '-likes_count', '-views')
    recommended_videos = Video.objects.filter(author__follow = request.user.id).annotate(likes_count=Count('likes')).order_by('-date_uploaded', '-likes_count', '-views')
    # print(recommended_articles)clear
    categories = Category.objects.all()
    channels = Channel.objects.all()
    data['articles'] = articles
    data['audios'] = audios
    data['videos'] = videos
    data['categories'] = categories
    data['channels'] = channels
    data['recommended_articles'] = recommended_articles
    data['recommended_audios'] = recommended_audios
    data['recommended_videos'] = recommended_videos
    return data

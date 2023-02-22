from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import ListView, DetailView, RedirectView
from ue_app.models.channel_model import Channel, Profile
from ue_app.models.article_model import MediumInfo, Article
from ue_app.models.audio_model import Audio
from ue_app.models.category_model import Category
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from ue_app.models.video_model import Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect

class ChannelDetailView(DetailView):
    model = Channel
    template_name = "main/channel_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Article.objects.all()
        audios = Audio.objects.all()
        videos = Video.objects.all()
        categories = Category.objects.all()
        channels = Channel.objects.all()

        context['article'] = self.object

        context['articles'] = articles
        context['audios'] = audios
        context['videos'] = videos
        context['categories'] = categories
        context['channels'] = channels

        return context

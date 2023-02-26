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
from django.utils.text import slugify
from django.urls import reverse_lazy

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


class ChannelFollowToggleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Channel, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.follow.all():
                obj.follow.remove(user)
            else:
                obj.follow.add(user)

        return url_


class ChannelFollowAPIToggleView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slug=None, format=None, *args, **kwargs):
        # slug = self.kwargs.get("slug")
        obj = get_object_or_404(Channel, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        following = False
        if user.is_authenticated:
            if user in obj.follow.all():
                # liked = False
                obj.follow.remove(user)
            else:
                following = True
                obj.follow.add(user)
                updated = True
        data = {
            'updated': updated,
            'following': following
        }
        
        return Response(data)
    

class ChannelCreateView(CreateView):
    model = Channel
    fields = ['display_name','description', 'banner', 'channel_logo']
    template_name = 'main/channel_form.html'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.display_name)
        form.instance.profile = Profile.objects.get(user=self.request.user)
        form.save()
        return super().form_valid(form)


class ChannelUpdateView(UpdateView):
    model = Channel
    fields = ['display_name','description', 'banner', 'channel_logo']
    template_name = 'main/channel_form.html'

class ChannelDeleteView(DeleteView):
    model = Channel
    success_url = reverse_lazy('ue_app:profile_detail')
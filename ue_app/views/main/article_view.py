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


class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    paginate_by = 10
    template_name = "main/article_list.html"

    def get_context_data(self, *args, **kwargs):

        # Call the base implementation first to get the context
        context = super(ArticleListView, self).get_context_data(**kwargs)

        articles = Article.objects.all()
        audios = Audio.objects.all()
        videos = Video.objects.all()
        categories = Category.objects.all()
        channels = Channel.objects.all()

        context['articles'] = articles
        context['audios'] = audios
        context['videos'] = videos
        context['categories'] = categories
        context['channels'] = channels

        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "main/article_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        session_key = f"viewed_article {self.object.slug}"
        if not self.request.session.get(session_key, False):
            self.object.views += 1
            self.object.save()
            self.request.session[session_key] = True

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

class ArticleLikeToggleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Article, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)

        return url_


class ArticleLikeAPIToggleView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slug=None, format=None, *args, **kwargs):
        # slug = self.kwargs.get("slug")
        obj = get_object_or_404(Article, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.likes.all():
                # liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
                updated = True
        data = {
            'updated': updated,
            'liked': liked
        }
        
        return Response(data)

class ArticleCreateView(CreateView):
    model = Article

    fields = ['title', 'feature_image', 'body', 'category', 'author', 'tags',
              'status', 'display']
    template_name = 'main/article_form.html'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.save()
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'feature_image', 'body', 'category', 'author', 'tags',
              'status', 'display']
    template_name = 'main/article_form.html'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('ue_app:channel_detail')

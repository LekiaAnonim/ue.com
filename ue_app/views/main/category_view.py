from django.views.generic import ListView, DetailView
from ue_app.models.channel_model import Channel
from ue_app.models.article_model import MediumInfo, Article
from ue_app.models.audio_model import Audio
from ue_app.models.category_model import Category
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from ue_app.models.video_model import Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect


class CategoryListView(ListView):
    model = Category
    context_object_name = "categories"
    paginate_by = 10
    template_name = "main/category_list.html"

    def get_context_data(self, *args, **kwargs):

        # Call the base implementation first to get the context
        context = super(CategoryListView, self).get_context_data(**kwargs)

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


class CategoryVideoView(ListView):
    model = Video
    template_name = "main/category_video.html"

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Video.objects.filter(category=category)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryVideoView,
                        self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        category_video = Video.objects.filter(category=category)

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
        context['category_video'] = category_video
        return context


class CategoryArticleView(ListView):
    model = Article
    template_name = "main/category_article.html"

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Article.objects.filter(category=category)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryArticleView,
                        self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        category_article = Article.objects.filter(category=category)

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
        context['category_article'] = category_article
        return context

class CategoryAudioView(ListView):
    model = Audio
    template_name = "main/category_audio.html"

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return Audio.objects.filter(category=category)

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryAudioView,
                        self).get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        category_audio = Audio.objects.filter(category=category)

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
        context['category_audio'] = category_audio
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = "main/category_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView,
                    self).get_context_data(**kwargs)

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


class CategoryCreateView(CreateView):
    model = Category


class CategoryUpdateView(UpdateView):
    model = Category

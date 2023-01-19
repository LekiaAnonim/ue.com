from django.views.generic import ListView, DetailView
from ue_app.models.channel_model import Channel
from ue_app.models.article_model import MediumInfo, Article
from ue_app.models.audio_model import Audio
from ue_app.models.category_model import Category
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from ue_app.models.video_model import Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ChannelListView(ListView):
    model = Channel
    context_object_name = "channel"
    paginate_by = 10
    template_name = "main/channel_list.html"

    def get_context_data(self, *args, **kwargs):

        # Call the base implementation first to get the context
        context = super(ChannelListView, self).get_context_data(**kwargs)

        articles = Articles.objects.all()
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


class ChannelDetailView(DetailView):
    model = Channel
    template_name = "account/channel_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        articles = Articles.objects.all()
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


class ChannelCreateView(CreateView):
    model = Channel


class ChannelUpdateView(UpdateView):
    model = Channel

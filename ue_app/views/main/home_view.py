from django.http import HttpResponse
import datetime
from django.views import View
from django.views.generic.base import TemplateView
from ue_app.models.channel_model import Channel
from ue_app.models.article_model import MediumInfo, Article
from ue_app.models.audio_model import Audio
from ue_app.models.category_model import Category
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from ue_app.models.video_model import Video
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect

class HomeView(TemplateView):

    template_name = 'main/index.html'

    context = {
        "login_form": AuthenticationForm()
    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all()
        audios = Audio.objects.all()
        videos = Video.objects.all()
        categories = Category.objects.all()
        channels = Channel.objects.all()
        # login_user = Profile.objects.filter(id=request.user.id)
        
        # context['login_user'] = login_user
        context['articles'] = articles
        context['audios'] = audios
        context['videos'] = videos
        context['categories'] = categories
        context['channels'] = channels
        context["login_form"]= AuthenticationForm()
        return context

    def post(self, request, *args, **kwargs):
    
        login_form = AuthenticationForm(request.POST)

        if login_form.is_valid():
            user = login_form.save(commit=False)
            user.save()
            login(request, user)
            messages.success(
                request, f'Hi {user.username}, Your login was successful!! .')

            return redirect('ue_app:home')

        else:
            messages.error(request, "Please provide valid information.")
            # Redirect user to register page
            return render(request, self.template_name, self.context)
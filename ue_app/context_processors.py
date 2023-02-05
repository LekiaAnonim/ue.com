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

def base_data(request):
    data = {}
    # MyForm(request.GET, user=request.user)
    data["register_form"] = UserRegisterForm()
    articles = Article.objects.all()
    audios = Audio.objects.all()
    videos = Video.objects.all()
    categories = Category.objects.all()
    channels = Channel.objects.all()
    # login_user = Profile.objects.filter(id=request.user.id)

    # context['login_user'] = login_user
    data['articles'] = articles
    data['audios'] = audios
    data['videos'] = videos
    data['categories'] = categories
    data['channels'] = channels
    # if request.method == 'POST':
    #     register_form = UserRegisterForm(request.POST)

    #     if register_form.is_valid():
    #         user = register_form.save(commit=False)
    #         user.is_active = True
    #         user.is_staff = True
    #         user.save()
    #         login(request, user)
    #         messages.success(
    #             request, f'Hi {user.username}, your registration was successful!! .')

    #         return redirect('ue_app:home')

    #     else:
    #         messages.error(request, "Please provide valid information.")
    #         # Redirect user to register page
    #         return render(request, 'main/base.html', data)
    return data

from django.views.generic import ListView, DetailView, RedirectView
from ue_app.models.channel_model import Channel, Profile
from ue_app.models.article_model import MediumInfo, Article
from ue_app.models.audio_model import Audio
from ue_app.forms.main.comment_form import VideoCommentForm
from ue_app.models.category_model import Category
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from ue_app.models.video_model import Video
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.http import HttpResponse
from django.http import JsonResponse


class VideoListView(ListView):
    model = Video
    context_object_name = "videos"
    paginate_by = 10
    template_name = "main/video_list.html"

    def get_context_data(self, *args, **kwargs):

        # Call the base implementation first to get the context
        context = super(VideoListView, self).get_context_data(**kwargs)


        articles = Article.objects.all()
        audios = Audio.objects.all()
        videos = Video.objects.all()
        categories = Category.objects.all()
        channels = Channel.objects.all()

        context['form'] = VideoCommentForm()
        context['articles'] = articles
        context['audios'] = audios
        context['videos'] = videos
        context['categories'] = categories
        context['channels'] = channels

        return context

from django.core.serializers import serialize
class VideoDetailCommentsView(DetailView):
    model = Video
    template_name = "main/video_detail_comments.html"
    # form_class = VideoCommentForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        video_comments = serialize('json', VideoComment.objects.all())
        
        context['video_comments'] = video_comments
        
        return context

    
    def render_to_response(self, context, **response_kwargs):
        if self.request.method == "GET":
            video_comments = context['video_comments']
            
            return JsonResponse(video_comments, safe=False)
        else:
            return super().render_to_response(context, **response_kwargs)
        
class VideoDetailView(DetailView):
    model = Video
    template_name = "main/video_detail.html"
    # form_class = VideoCommentForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        session_key = f"viewed_video {self.object.slug}"
        if not self.request.session.get(session_key, False):
            self.object.views += 1
            self.object.save()
            self.request.session[session_key] = True

        articles = Article.objects.all()
        audios = Audio.objects.all()
        videos = Video.objects.all()
        categories = Category.objects.all()
        channels = Channel.objects.all()
        video_comments = VideoComment.objects.filter(parent__isnull=True).order_by('-date_created')

        video_comment_replies = VideoComment.objects.exclude(parent__isnull=True).order_by('-date_created')

        context['articles'] = articles
        context['audios'] = audios
        context['videos'] = videos
        context['categories'] = categories
        context['channels'] = channels
        context['video_comments'] = video_comments
        context['video_comment_replies'] = video_comment_replies
        return context

    # def render_to_response(self, context, **response_kwargs):
    #     if self.request.method == "GET":
    #         video_comments = list(context['video_comments'].values())
    #         return JsonResponse(video_comments, safe=False)
    #     else:
    #         return super().render_to_response(context, **response_kwargs)
        
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        comment = request.POST['comment']
        user= request.user
        if request.POST.get('parent_comment', None)==None:

            parent = request.POST.get('parent_comment', None)
            
            new_comment = VideoComment(comment=comment,user=user, video=self.object, parent=parent)
            new_comment.save()

        # video_comments = VideoComment.objects.all()

        
        # reply = request.POST['reply']
        
        # print(parent)
        # for parent_comment in video_comments:
            # print(parent_comment.id)
            # if parent_comment.pk == parent:
        else:
            parent = request.POST['parent_comment']
            parent_cc = get_object_or_404(VideoComment, pk=parent)
            new_reply = VideoComment(comment=comment,user=user, video=self.object, parent=parent_cc)
            new_reply.save()
        return JsonResponse('New comment added', safe=False)

    def form_valid(self, form):
        
        form.save()
        return super(VideoDetailView, self).form_valid(form)




class VideoLikeToggleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        obj = get_object_or_404(Video, slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        if user.is_authenticated:
            if user in obj.likes.all():
                obj.likes.remove(user)
            else:
                obj.likes.add(user)

        return url_


class VideoLikeAPIToggleView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, slug=None, format=None, *args, **kwargs):
        # slug = self.kwargs.get("slug")
        obj = get_object_or_404(Video, slug=slug)
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


class VideoCreateView(CreateView):
    model = Video
    fields = ['title', 'video_upload', 'category', 'author', 'tags',
              'status', 'display', 'video_description']
    template_name = 'main/video_form.html'

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        form.save()
        return super().form_valid(form)

class VideoUpdateView(UpdateView):
    model = Video
    fields = ['title', 'video_upload', 'category', 'author', 'tags',
              'status', 'display', 'video_description']

    template_name = 'main/video_form.html'

class VideoDeleteView(DeleteView):
    model = Video
    success_url = reverse_lazy('ue_app:channel_detail')

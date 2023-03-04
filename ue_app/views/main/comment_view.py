from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from ue_app.forms.main.comment_form import VideoCommentForm
class VideoCommentCreateView(CreateView):
    model = VideoComment
    fields = ['comment']
    template_name = 'main/video_detail.html'

    

from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin

class VideoCommentFormView(SingleObjectMixin, FormView):
    template_name = 'main/video_detail.html'
    form_class = VideoCommentForm
    model = VideoComment
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
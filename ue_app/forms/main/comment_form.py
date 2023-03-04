from django import forms
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment

class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = VideoComment
        fields = ('comment',)
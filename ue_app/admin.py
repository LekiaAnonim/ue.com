from django.contrib import admin
from ue_app.models.channel_model import Channel, Profile
from ue_app.models.article_model import MediumInfo, Article
from ue_app.models.audio_model import Audio
from ue_app.models.category_model import Category
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from ue_app.models.video_model import Video

# Register your models here.

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    fields = ('profile', 'display_name', 'slug',
              'description', 'banner', 'channel_logo','follow')
    list_display = ('profile', 'display_name', 'slug',
                    'description', 'banner', 'channel_logo')
    list_filter = ("display_name",)
    search_fields = ("display_name",)
    prepopulated_fields = {'slug': ('display_name',)}
    empty_value_display = '-None-'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'photo', 'bio',
              'address', 'city', 'region', 'country', 'email_confirmed')
    list_display = ('user', 'first_name', 'last_name', 'phone_number',
                    'address', 'city', 'region', 'country', 'date_of_birth', 'photo', 'bio', 'email_confirmed')
    list_filter = ("user",)
    search_fields = ("user",)
    empty_value_display = '-None-'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name',]
    empty_value_display = '-None-'


@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.action(description='Mark selected stories as draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


@admin.action(description='Mark selected stories as public')
def make_public(modeladmin, request, queryset):
    queryset.update(display='pu')


@admin.action(description='Mark selected stories as private')
def make_private(modeladmin, request, queryset):
    queryset.private(display='pr')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'feature_image', 'body', 'category', 'slug', 'author', 'tags',
              'status', 'display', 'views', 'verify', 'likes')
    list_display = ('title', 'feature_image', 'body', 'category', 'slug', 'author', 'tags',
                    'status', 'display', 'views', 'verify')
    exclude = ['date_uploaded', 'date_updated']
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = '-None-'
    actions = [make_published, make_draft, make_public, make_private]



@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    fields = ('title', 'feature_image', 'audio_description', 'audio_upload', 'category', 'slug', 'author', 'tags',
              'status', 'display', 'views', 'verify', 'likes')
    list_display = ('title', 'feature_image', 'audio_description', 'audio_upload', 'category', 'slug', 'author',
                    'status', 'display', 'views', 'verify')
    exclude = ['date_uploaded', 'date_updated']
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = '-None-'
    actions = [make_published, make_draft, make_public, make_private]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    fields = ('title', 'video_description', 'video_upload', 'category', 'slug', 'author', 'tags',
              'status', 'display', 'views', 'verify', 'likes')
    list_display = ('title','video_description', 'video_upload', 'category', 'slug', 'author',
                    'status', 'display', 'views', 'verify')
    exclude = ['date_uploaded', 'date_updated']
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = '-None-'
    actions = [make_published, make_draft, make_public, make_private]


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('article','user', 'comment', 'parent',
                    'date_created', 'approved', 'article')
    exclude = ['date_created', 'date_updated']
    empty_value_display = '-None-'


@admin.register(AudioComment)
class AudioCommentAdmin(admin.ModelAdmin):
    list_display = ('audio','user', 'comment', 'parent',
                    'date_created', 'approved')
    exclude = ['date_created', 'date_updated']
    empty_value_display = '-None-'


@admin.register(VideoComment)
class VideoCommentAdmin(admin.ModelAdmin):
    list_display = ('video','user', 'comment', 'parent',
                    'date_created', 'approved')
    exclude = ['date_created', 'date_updated']
    empty_value_display = '-None-'

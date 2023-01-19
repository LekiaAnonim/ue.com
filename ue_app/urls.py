from django.urls import path
from ue_app.views.main import home_view
from ue_app.views.main import article_view
from ue_app.views.main import audio_view
from ue_app.views.main import category_view
from ue_app.views.main import video_view

app_name = "ue_app"

urlpatterns = [
    path('', home_view.HomeView.as_view(), name='home'),
    path(
        route='writen-stories/',
        view=article_view.ArticleListView.as_view(),
        name='articles'
    ),
    path(
        route='writen-stories/<str:username>/<str:slug>',
        view=article_view.ArticleDetailView.as_view(),
        name='article_detail'
    ),
    path(
        route='writen-stories/<str:username>/<str:slug>/like',
        view=article_view.ArticleLikeToggleView.as_view(),
        name='article_like_toggle'
    ),
    path(
        route='api/writen-stories/<str:username>/<str:slug>/like',
        view=article_view.ArticleLikeAPIToggleView.as_view(),
        name='article_api_like_toggle'
    ),
    path(
        route='writen-stories/create',
        view=article_view.ArticleCreateView.as_view(),
        name='article_create'
    ),
    path(
        route='writen-stories/@<str:username>/<str:slug>/update',
        view=article_view.ArticleUpdateView.as_view(),
        name='article_update'
    ),

    # Audio URL
    path(
        route='audio-stories/',
        view=audio_view.AudioListView.as_view(),
        name='audios'
    ),
    path(
        route='audio-stories/@<str:username>/<str:slug>',
        view=audio_view.AudioDetailView.as_view(),
        name='audio_detail'
    ),
    path(
        route='audio-stories/create',
        view=audio_view.AudioCreateView.as_view(),
        name='audio_create'
    ),
    path(
        route='audio-stories/@<str:username>/<str:slug>/update',
        view=audio_view.AudioUpdateView.as_view(),
        name='audio_update'
    ),
    path(
        route='audio-stories/<str:username>/<str:slug>/like',
        view=audio_view.AudioLikeToggleView.as_view(),
        name='audio_like_toggle'
    ),
    path(
        route='api/audio-stories/<str:username>/<str:slug>/like',
        view=audio_view.AudioLikeAPIToggleView.as_view(),
        name='audio_api_like_toggle'
    ),

    # Video URL
    path(
        route='video-stories/',
        view=video_view.VideoListView.as_view(),
        name='videos'
    ),
    path(
        route='video-stories/@<str:username>/<str:slug>',
        view=video_view.VideoDetailView.as_view(),
        name='video_detail'
    ),
    path(
        route='video-stories/<str:username>/<str:slug>/like',
        view=video_view.VideoLikeToggleView.as_view(),
        name='video_like_toggle'
    ),
    path(
        route='api/video-stories/<str:username>/<str:slug>/like',
        view=video_view.VideoLikeAPIToggleView.as_view(),
        name='video_api_like_toggle'
    ),
    path(
        route='video-stories/create',
        view=video_view.VideoCreateView.as_view(),
        name='video_create'
    ),
    path(
        route='video-stories/@<str:username>/<str:slug>/update',
        view=video_view.VideoUpdateView.as_view(),
        name='video_update'
    ),

    # Category URl 
    path(
        route='categories/',
        view=category_view.CategoryListView.as_view(),
        name='categories'
    ),
    path(
        route='category/<str:slug>',
        view=category_view.CategoryDetailView.as_view(),
        name='category_detail'
    ),
    path(
        route='category-videos/<str:slug>',
        view=category_view.CategoryVideoView.as_view(),
        name='category_videos'
    ),
    path(
        route='category-audios/<str:slug>',
        view=category_view.CategoryAudioView.as_view(),
        name='category_audios'
    ),
    path(
        route='category-articles/<str:slug>',
        view=category_view.CategoryArticleView.as_view(),
        name='category_articles'
    ),
    path(
        route='category/create',
        view=category_view.CategoryCreateView.as_view(),
        name='category_create'
    ),
    path(
        route='writen-stories/@<str:username>/<str:slug>/update',
        view=article_view.ArticleUpdateView.as_view(),
        name='article_update'
    ),

    # Channel
]

from django.urls import path
from ue_app.views.main import home_view
from ue_app.views.main import article_view
from ue_app.views.main import audio_view
from ue_app.views.main import category_view
from ue_app.views.main import video_view, channel_view, profile_view
from ue_app.views.authentication import registration_view
from ue_app.views.authentication import login_view
from ue_app.views.authentication import password_reset_view
from django.contrib.auth import views as auth_views

app_name = "ue_app"

urlpatterns = [
    path('', home_view.HomeView.as_view(), name='home'),
    path(
        route='written-stories/',
        view=article_view.ArticleListView.as_view(),
        name='articles'
    ),
    path(
        route='written-stories/<str:username>/<str:slug>',
        view=article_view.ArticleDetailView.as_view(),
        name='article_detail'
    ),
    path(
        route='written-stories/<str:username>/<str:slug>/like',
        view=article_view.ArticleLikeToggleView.as_view(),
        name='article_like_toggle'
    ),
    path(
        route='api/written-stories/<str:username>/<str:slug>/like',
        view=article_view.ArticleLikeAPIToggleView.as_view(),
        name='article_api_like_toggle'
    ),
    path(
        route='written-stories/create',
        view=article_view.ArticleCreateView.as_view(),
        name='article_create'
    ),
    path(
        route='written-stories/@<str:username>/<str:slug>/update',
        view=article_view.ArticleUpdateView.as_view(),
        name='article_update'
    ),
    path(
        route='written-stories/@<str:username>/<str:slug>/delete',
        view=article_view.ArticleDeleteView.as_view(),
        name='article_delete'
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
        route='audio-stories/@<str:username>/<str:slug>/delete',
        view=audio_view.AudioDeleteView.as_view(),
        name='audio_delete'
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
    path(
        route='video-stories/@<str:username>/<str:slug>/delete',
        view=video_view.VideoDeleteView.as_view(),
        name='video_delete'
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
    path(
        route='written-stories/@<str:username>/<str:slug>/delete',
        view=article_view.ArticleDeleteView.as_view(),
        name='article_delete'
    ),

    # Channel
    path(
        route='channel/@<str:username>/<str:slug>',
        view=channel_view.ChannelDetailView.as_view(),
        name='channel_detail'
    ),
    path(
        route='channel/<str:username>/<str:slug>/follow',
        view=channel_view.ChannelFollowToggleView.as_view(),
        name='channel_follow_toggle'
    ),
    path(
        route='api/channel/<str:username>/<str:slug>/follow',
        view=channel_view.ChannelFollowAPIToggleView.as_view(),
        name='channel_api_follow_toggle'
    ),
    path(
        route='channel/create',
        view=channel_view.ChannelCreateView.as_view(),
        name='channel_create'
    ),
    path(
        route='channel/@<str:username>/<str:slug>/update',
        view=channel_view.ChannelUpdateView.as_view(),
        name='channel_update'
    ),
    path(
        route='channel/@<str:username>/<str:slug>/delete',
        view=channel_view.ChannelDeleteView.as_view(),
        name='channel_delete'
    ),


     # Profile
    path(
        route='profile/@<str:username>/<int:pk>',
        view=profile_view.ProfileDetailView.as_view(),
        name='profile_detail'
    ),
    path(
        route='profile/create',
        view=profile_view.ProfileCreateView.as_view(),
        name='profile_create'
    ),
    path(
        route='profile/@<str:username>/update',
        view=profile_view.ProfileUpdateView.as_view(),
        name='profile_update'
    ),
    
    

    # Signup and SignIn URL
    path(
        route='signup',
        view=registration_view.UserRegisterView.as_view(),
        name='signup'
    ),
    path(
        route='email-verification-confirm',
        view=registration_view.EmailVerificationConfirm.as_view(),
        name='email_verification_confirm'
    ),
    path(
        route='email-verification/invalid-link',
        view=registration_view.EmailVerificationInvalid.as_view(),
        name='email_verification_invalid'
    ),
    path(
        route='login',
        view=login_view.UserLoginView.as_view(),
        name='login'
    ),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    # Reset Password URLS

    path(
        route='reset-password',
        view=password_reset_view.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path('password-reset/done/', password_reset_view.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         password_reset_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset_complete/done/', password_reset_view.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('password-change', password_reset_view.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', password_reset_view.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('activate/<uidb64>/<token>/',
         registration_view.activate, name='activate'),

]

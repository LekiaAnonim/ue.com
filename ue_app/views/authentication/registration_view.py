
from .tokens import account_activation_token
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from ue_app.forms.authentication.registration_form import UserRegisterForm
from ue_app.models.channel_model import Channel
from ue_app.models.article_model import MediumInfo, Article
from ue_app.models.audio_model import Audio
from ue_app.models.category_model import Category
from ue_app.models.comment_model import Comment, ArticleComment, AudioComment, VideoComment
from ue_app.models.video_model import Video
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.conf import settings
UserModel = get_user_model()


class UserRegisterView(View):
    """
      View to let users register
    """
    template_name = 'registration/register.html'
    context = {
        "register_form": UserRegisterForm()
    }

    def get(self, request):
        success_message = "Successful"
        articles = Article.objects.all()
        audios = Audio.objects.all()
        videos = Video.objects.all()
        categories = Category.objects.all()
        channels = Channel.objects.all()

        self.context['success_message'] = success_message
        self.context['articles'] = articles
        self.context['audios'] = audios
        self.context['videos'] = videos
        self.context['categories'] = categories
        self.context['channels'] = channels

        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):

        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = True
            user.is_staff = True
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('registration/activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
                'protocol': 'http',
            })
            from_email = settings.EMAIL_HOST_USER
            to_email = register_form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, from_email, to=[to_email]
            )
            email.send()

            return reverse_lazy('ue_app:email_verification_confirm')

        else:
            messages.error(request, "Please provide valid information.")
            # Redirect user to register page
            return render(request, self.template_name, self.context)

    def get_success_url(self):
        return reverse('ue_app:home')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(
            request, f'Hi {user.username}, your registration was successful!! .')
        return reverse('ue_app:home')
    else:
        return reverse_lazy('ue_app:email_verification_invalid')


class EmailVerificationConfirm(TemplateView):
    template_name = 'registration/email_verification_confirm.html'


class EmailVerificationInvalid(TemplateView):
    template_name = 'registration/email_verification_invalid.html'

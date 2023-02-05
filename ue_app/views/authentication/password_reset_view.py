from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import (PasswordResetDoneView, PasswordResetConfirmView,
                                        PasswordResetCompleteView, PasswordChangeView,
                                       PasswordChangeDoneView, PasswordResetView)
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.views.generic import View
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.urls import reverse_lazy

class PasswordResetView(PasswordResetView):
    template_name = 'registration/pwd_reset_form.html'
    email_template_name = "registration/email_text/password_reset_email.html"
    from_email = 'lekiaprosper@gmail.com'
    subject_template_name = "registration/email_text/password_reset_subject.txt"
    success_url = reverse_lazy("ue_app:password_reset_done")

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/email_text/password_reset_done.html' 

class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/email_text/password_reset_confirm.html'
    success_url = reverse_lazy("ue_app:password_reset_complete")

class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/email_text/password_reset_complete.html'

class PasswordChangeView(PasswordChangeView):
    template_name = 'registration/email_text/password_change_form.html'
    success_url = reverse_lazy("ue_app:password_change_done")

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/email_text/password_change_done.html'

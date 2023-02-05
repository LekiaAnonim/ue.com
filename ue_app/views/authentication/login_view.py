from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

class UserLoginView(View):
    """
     Logs author into dashboard.
    """
    template_name = 'registration/login.html'
    context_object = {"login_form": AuthenticationForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            
            login(request, user)
            messages.success(request, f"Login Successful ! "
                                f"Welcome {user.username}. Update your User profile if you have not done so. Ignore this message if your User profile is upto date.")
            return redirect('ue_app:home')

        else:
            messages.error(request,
                           f"Please enter a correct username and password. Note that both fields may be case-sensitive."
                           )
            return render(request, self.template_name, self.context_object)

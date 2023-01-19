
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from ue_app.forms.authentication.registration_form import UserRegisterForm
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

        self.context['success_message'] = success_message

        self.context['vendors'] = Vendor.objects.all()
        self.context['categories'] = Category.objects.all()
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):

        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = True
            user.is_staff = True
            user.save()
            login(request, user)
            messages.success(
                request, f'Hi {user.username}, your registration was successful!! .')

            return redirect('showcase:enrol-customer-create')

        else:
            messages.error(request, "Please provide valid information.")
            # Redirect user to register page
            return render(request, self.template_name, self.context_object)

    def get_success_url(self):
        return reverse('showcase:enrol-customer-create')

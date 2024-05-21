from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import CreateView, TemplateView

from users.forms import CustomUserCreationForm
from users.models import User
from users.utils import account_activation_token, randomword


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(self.request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(self.request, 'users/verification_request.html')

        return super().form_valid(form)


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'users/account_activated.html')
    else:
        return render(request, 'users/invalid_link.html')

class PasswordResetView(TemplateView):
    template_name = 'users/new_password_request.html'

    def post(self, request):
        user_email = request.POST.get('email')
        user = User.objects.get(email=user_email)
        new_password = randomword(12)
        user.set_password(new_password)

        message = render_to_string('users/new_password_email.html', {
            'user': user_email,
            'new_password': new_password
        })
        email = EmailMessage(
            'Your new password', message, to=[user_email]
        )
        email.send()

        user.save()
        return render(request, 'users/new_password_sent.html')
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def index(request):
    projects = Project.objects.all()
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_fullname = form.cleaned_data.get('fullname')
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        to_email = [settings.EMAIL_HOST_USER]
        send_mail('Contact form message', form_message, form_email, to_email, fail_silently=False)
        print(form.cleaned_data)

    context = {
        'projects': projects,
        'form': form,
    }

    return render(request, 'portofolio/layout.html', context)

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    #projects = Project.objects.all()
    projects = Project.objects.order_by('project_date')[:6]
    form = ContactForm(request.POST or None)

    context = {
        'projects': projects,
        'form': form,
    }

    if form.is_valid():
        form_fullname = form.cleaned_data.get('fullname')
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        from_email = 'rsdjasdjasdl@jskjdsd.com'
        to_email = [settings.EMAIL_HOST_USER]
        send_mail('Contact form message', form_message, from_email, to_email, fail_silently=False)

    return render(request, 'layout.html', context)

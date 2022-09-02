from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import ContactForm
from .models import Project


def IndexView(request):
    return render(request, 'naturegraphics/index.html')

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
            return render(request, 'naturegraphics/success.html')
        else:
            return render(request, 'naturegraphics/failure.html')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'naturegraphics/contact.html', context)

class ProjectsView(generic.ListView):
    model = Project
    template_name = 'naturegraphics/projects.html'
    context_object_name = 'project_images'

    def get_queryset(self):
        return Project.objects.all().order_by('order')
    


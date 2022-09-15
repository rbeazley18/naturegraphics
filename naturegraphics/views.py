from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .forms import ContactForm
from .models import Portfolio, Gallery, Project1, Project2, Project3, Project4


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

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'naturegraphics/portfolio.html'
    context_object_name = 'portfolio'

    def get_queryset(self):
        return Portfolio.objects.all().order_by('order')

class GalleryView(generic.ListView):
    model = Gallery
    template_name = 'naturegraphics/gallery.html'
    context_object_name = 'gallery'

    def get_queryset(self):
        return Gallery.objects.all().order_by('order')

class Project1View(generic.ListView):
    model = Project1
    template_name = 'naturegraphics/project1.html'
    context_object_name = 'project1'

    def get_queryset(self):
        return Project1.objects.all().order_by('order')

class Project2View(generic.ListView):
    model = Project2
    template_name = 'naturegraphics/project2.html'
    context_object_name = 'project2'

    def get_queryset(self):
        return Project2.objects.all().order_by('order')

class Project3View(generic.ListView):
    model = Project3
    template_name = 'naturegraphics/project3.html'
    context_object_name = 'project3'

    def get_queryset(self):
        return Project3.objects.all().order_by('order')

class Project4View(generic.ListView):
    model = Project4
    template_name = 'naturegraphics/project4.html'
    context_object_name = 'project4'

    def get_queryset(self):
        return Project4.objects.all().order_by('order')
    

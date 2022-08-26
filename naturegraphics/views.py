from django.shortcuts import render
from django.http import HttpResponse


def IndexView(request):
    return render(request, 'naturegraphics/index.html')

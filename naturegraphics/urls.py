from django.urls import path

from . import views

app_name = 'naturegraphics'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('contact', views.ContactView, name='contact'),
    path('culturalhistory', views.Project1View.as_view(), name='culturalhistory'),
    path('naturalhistory', views.Project2View.as_view(), name='naturalhistory'),
    path('parkinformation', views.Project3View.as_view(), name='parkinformation'),
    path('resourcemanagement', views.Project4View.as_view(), name='resourcemanagement'),
]
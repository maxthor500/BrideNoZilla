from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact', views.contact_me, name='contact'),
    path('about', views.about_me, name="about")
]

from django.shortcuts import render

# Create your views here


def index(request):
    """ A view to return the index page. """
    return render(request, 'home/index.html')


def contact_me(request):
    """ A view to return the contact me page. """
    return render(request, 'home/contact.html')


def about_me(request):
    """ A view to return the about me page. """
    return render(request, 'home/about.html')
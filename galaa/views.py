from django.shortcuts import render
from django.http  import HttpResponse
from .models import photos

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    photo= photos.objects.all()
    return render(request, 'all-gala/index.html',{'photo':photo})


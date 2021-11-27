from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import photos
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def index(request):
    photo= photos.objects.all()
    return render(request, 'all-gala/index.html',{'photo':photo})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photo = photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gala/search.html',{"message":message,"photo": searched_photo})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gala/search.html',{"message":message})

def photo(request,photo_id):
    try:
        article = photo.objects.get(id = photo_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-gala/photo.html", {"article":article})


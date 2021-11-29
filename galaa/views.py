from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .models import photos,Category,Location
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')



def index(request):
    categories = Category.objects.all()
    location = Location.objects.all()
    if 'location' in request.GET and request.GET["location"]:
        location_id = request.GET.get("location")
        photo = photos.objects.filter(location = location_id)
    elif 'category' in request.GET and request.GET["category"]:
        category_id = request.GET.get("category")
        photo = photos.objects.filter(category = category_id)
    else:
     photo= photos.objects.all()
    return render(request, 'all-gala/index.html',{'photo':photo,'categories':categories, 'location':location})



def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photo = photos.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gala/search.html',{"message":message,"photo": searched_photo})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gala/search.html',{"message":message})




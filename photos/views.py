from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt
from django.http import Http404
from .models import Image


# Create your views here.
def welcome(request):
    title='Gallery Webpage'
    images= Image.objects.all()
    return render(request, 'all-photos/image.html',{"images":images, "title":title})



def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_Category(search_term)

        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message})


def image(request,image_id):
    try:
        images = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image_details.html", {"images":images})

from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "index.html")

def songs_cat_page(request,category):
    return render(request, "categories.html", {
        "cat" : category
    })

def songs_page(request):
    pass

def song_page(request):
    pass

def artists_page(request):
    pass

def artist_page(request):
    pass
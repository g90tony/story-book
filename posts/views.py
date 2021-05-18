from django.shortcuts import render
from .models import Category, Location, Photo 
# Create your views here.
def index(request):
    title = "Home: Welcome to Story Book"
    allPosts = Photo.objects.all()
    
    return render(request, 'home.html', {"title":title ,"posts": allPosts})

def search_title(request, search_query):
    
    title = f'Search: {search_query} Results'
    
    Photo.objects.filter(category = search_query)
    
    return render(request, 'search.html', {"title": title})
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def search_title(request):
    return render(request, 'search.html')
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='Home'),
    re_path('^search/<search_query>$', views.search_categories, name='Search'),
    re_path('^filer/<location_filter>$', views.search_categories, name='Filter Location'),
]

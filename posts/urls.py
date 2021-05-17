from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.login, name='Sign In'),
    re_path('^register$', views.register, name='Sign Up')
]

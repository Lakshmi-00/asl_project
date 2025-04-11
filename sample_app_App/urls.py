import stat
from django.urls import path

from sample_app_project import settings
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
]

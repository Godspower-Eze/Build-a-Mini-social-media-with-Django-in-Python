from django.urls import path
from .views import home, post_create

urlpatterns = [
    path('', home, name='home'),
    path('new/', post_create, name='newpost')
]
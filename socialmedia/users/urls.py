from django.urls import path
from .views import user_creation

urlpatterns = [
    path('create_account/', user_creation, name='usercreation')
]
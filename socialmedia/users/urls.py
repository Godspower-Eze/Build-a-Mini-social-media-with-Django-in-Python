from django.urls import path
from .views import user_creation, user_login, user_logout

urlpatterns = [
    path('create_account/', user_creation, name='usercreation'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout')
]
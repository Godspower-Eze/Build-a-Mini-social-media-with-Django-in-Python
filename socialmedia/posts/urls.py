from django.urls import path
from .views import home, post_create, post_detail, update_post, delete_post

urlpatterns = [
    path('', home, name='home'),
    path('new/', post_create, name='newpost'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),
    path('update/<int:post_id>/', update_post, name='post_update'),
    path('delete/<int:post_id>/', delete_post, name='post_delete')
]
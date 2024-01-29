from django.urls import path
from . import views

urlpatterns = [
    
    path('get_todo/' , views .get_todo),
    path('post-todo/' , views .post_todo),
    path('patch_todo', views .patch_todo),
    path('delete_todo/' , views.delete_todo),

]
from django.urls import path
from .views import get_todos,create_todos,update_todo,delete_todo
urlpatterns=[
    path('todos/',get_todos),
    path('create/',create_todos),
    path('update/<int:pk>',update_todo),
    path('delete/<int:pk>',delete_todo),



]
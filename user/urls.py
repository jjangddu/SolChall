from django.urls import path
from . import views
from .views import getUser, postUser, update, delete, deleteById

urlpatterns = [
    path('get/', getUser),
    path('post/', postUser),
    path('update/<int:id>/', update),
    path('delete/', delete),
    path('delete/<int:id>/',deleteById),
]

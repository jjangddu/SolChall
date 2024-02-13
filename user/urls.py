from django.urls import include, path
from . import views
from .views import getUser, postUser, update, delete, deleteById
from rest_framework import routers

router = routers.DefaultRouter()
router.register('User',views.UserViewSet)

urlpatterns = [
    path('get/', getUser),
    path('post/', postUser),
    path('update/<int:id>/', update),
    path('delete/', delete),
    path('delete/<int:id>/',deleteById),
    # path('', include(router.urls)),
]

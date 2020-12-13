from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import  CreateUserView, MyProfileView, BoardViewSet, ListViewSet, CardViewSet

router = routers.DefaultRouter()
router.register('board', BoardViewSet, basename='board')
router.register('list', ListViewSet, basename='list')
router.register('card', CardViewSet, basename='card')

urlpatterns = [
    path('', include(router.urls)),
    path('myself/', MyProfileView.as_view(), name='myself'),
    path('register/', CreateUserView.as_view(), name='register'),

]


from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('accounts', views.AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserView.as_view(), name='user-register')
]
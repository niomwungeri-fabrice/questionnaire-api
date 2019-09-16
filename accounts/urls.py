
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.CreateAccountView.as_view(),
         name='user-register'),
    path('users/', views.UserListView.as_view(),
         name='user-list'),
    path('users/<uuid:id>/', views.UserDetailView.as_view(),
         name='user-detail')
]

from django.urls import path

from . import views

app_name = 'meetups'

urlpatterns = [
    path('meetup/new/', views.CreateMeetUpView.as_view(),
         name='create-meetup'),
    path('meetup/<str:id>/', views.MeetUpDetailView.as_view(),
         name='detail-meetup'),
    path('meetup/', views.MeetUpListView.as_view(),
         name='list-meetups'),
    path('tags/', views.CreateTagView.as_view(),
         name='create-list-tags')
]

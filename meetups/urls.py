from django.urls import path

from . import views

app_name = 'meetups'

urlpatterns = [
    path('meetups/new/', views.CreateMeetUpView.as_view(),
         name='create-meetup'),
    path('meetups/', views.MeetUpListView.as_view(),
         name='list-meetups'),
    path('meetups/upcoming/', views.UpcomingMeetUPsView.as_view(),
         name='upcoming-meetups'),     # precedence issues to be fixed
    path('meetups/<str:id>/', views.MeetUpDetailView.as_view(),
         name='detail-meetup'),
    path('tags/', views.CreateTagView.as_view(),
         name='create-list-tags')
]

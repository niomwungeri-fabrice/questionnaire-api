from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meetups', views.MeetUpViewSet)
router.register('tags', views.TagViewSet)

urlpatterns = router.urls

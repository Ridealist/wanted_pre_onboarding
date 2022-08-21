from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from recruit.announce.views import AnnouncementViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("announce", AnnouncementViewSet, basename="announce")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]
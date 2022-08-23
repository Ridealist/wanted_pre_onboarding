from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recruit.announce.views import AnnouncementViewSet
from recruit.apply.views import ApplyViewSet

router = DefaultRouter()


router.register("announce", AnnouncementViewSet, basename="Announce")
router.register("apply", ApplyViewSet, basename="Apply")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]

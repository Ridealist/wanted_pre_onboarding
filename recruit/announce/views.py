from rest_framework.viewsets import ModelViewSet

from recruit.announce.models import Announcement
from recruit.announce.serializers import (
    AnnounceRegisterSerializer,
    AnnounceListSerializer,
    AnnounceDetailSerializer,
)


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnounceRegisterSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AnnounceListSerializer
        elif self.action == "retrieve":
            return AnnounceDetailSerializer
        else:
            return self.serializer_class

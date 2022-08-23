from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from recruit.announce.models import Announcement
from recruit.announce.serializers import (
    AnnounceRegisterSerializer,
    AnnounceListSerializer,
    AnnounceDetailSerializer,
)


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnounceRegisterSerializer
    filter_backends = [SearchFilter]
    search_fields = ["company__name", "position", "technology"]

    def get_serializer_class(self):
        if self.action == "list":
            return AnnounceListSerializer
        elif self.action == "retrieve":
            return AnnounceDetailSerializer
        else:
            return self.serializer_class

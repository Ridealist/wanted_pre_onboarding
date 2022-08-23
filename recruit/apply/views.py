from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from .models import Apply
from .serializers import ApplySerializer


class ApplyViewSet(GenericViewSet, CreateModelMixin):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer

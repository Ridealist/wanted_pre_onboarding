from rest_framework.generics import ListCreateAPIView

from .models import Apply
from .serializers import ApplySerializer


class ApplyListCreateView(ListCreateAPIView):
    queryset = Apply.objects.all()
    serializer_class = ApplySerializer

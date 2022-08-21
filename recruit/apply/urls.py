from django.urls import path
from .views import ApplyListCreateView

app_name = "apply"
urlpatterns = [
    path("", ApplyListCreateView.as_view(), name="apply-create"),
]

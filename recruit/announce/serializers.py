from rest_framework import serializers
from recruit.announce.models import Announcement, Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class AnnouncementSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Announcement
        fields = "__all__"

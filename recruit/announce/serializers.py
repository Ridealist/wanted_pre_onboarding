from rest_framework import serializers
from recruit.announce.models import Announcement, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class AnnounceRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [
            "company",
            "position",
            "credit",
            "description",
            "technology",
        ]


class AnnounceListSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Announcement
        fields = [
            "id",
            "company",
            "position",
            "credit",
            "technology",
        ]


class AnnounceDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    additional = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = [
            "id",
            "company",
            "position",
            "credit",
            "technology",
            "description",
            "additional",
        ]

    def get_additional(self, obj):
        queryset = Announcement.objects.filter(company=obj.company).exclude(
            id=obj.id
        )
        return [query.id for query in queryset]

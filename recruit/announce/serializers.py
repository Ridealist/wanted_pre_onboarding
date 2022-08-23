from rest_framework import serializers
from recruit.announce.models import Announcement, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            "name",
            "country",
            "region",
        ]


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
    announce_set = serializers.SerializerMethodField()

    class Meta:
        model = Announcement
        fields = [
            "id",
            "company",
            "position",
            "credit",
            "technology",
            "description",
            "announce_set",
        ]

    def get_announce_set(self, obj):
        queryset = Announcement.objects.filter(company=obj.company).exclude(
            id=obj.id
        )
        return [query.id for query in queryset]

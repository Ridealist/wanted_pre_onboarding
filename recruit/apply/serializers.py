from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

from .models import Apply


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = [
            "announce",
            "applicant",
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Apply.objects.all(), fields=["announce", "applicant"]
            )
        ]

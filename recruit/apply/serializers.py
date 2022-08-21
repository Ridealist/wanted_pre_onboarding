from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

from .models import Apply


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Apply.objects.all(), fields=["announce", "applicant"]
            )
        ]

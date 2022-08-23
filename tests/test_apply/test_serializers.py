from django.test import TestCase
from rest_framework.exceptions import ValidationError

from recruit.apply.models import Apply
from recruit.apply.serializers import ApplySerializer
from tests.factories import UserFactory, AnnounceFactory


class ApplySerializerTests(TestCase):
    """Test for unique together validtor in serializer"""

    def setUp(self):
        self.user_1 = UserFactory.create()
        self.user_2 = UserFactory.create()
        self.announce = AnnounceFactory.create()
        # instance create
        Apply.objects.create(applicant=self.user_1, announce=self.announce)

    def test_apply_unique_together_validator(self):
        # one field missing raise exception
        data = {
            "applicant": self.user_2.id,
        }
        with self.assertRaises(ValidationError):
            serializer = ApplySerializer(data=data)
            serializer.is_valid(raise_exception=True)

        # duplicate instance create raise exception
        data = {
            "applicant": self.user_1.id,
            "announce": self.announce.id,
        }
        with self.assertRaises(ValidationError):
            serializer = ApplySerializer(data=data)
            serializer.is_valid(raise_exception=True)

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.exceptions import ValidationError

from tests.factories import AnnounceFactory, UserFactory
from recruit.apply.models import Apply


class ApplyViewSetHTTPTests(TestCase):
    """Test for HTTP methods in ViewSet"""

    def setUp(self):
        self.user = UserFactory.create()
        self.announce = AnnounceFactory.create()
        self.url = reverse("api:Apply-list")
        self.client = APIClient()
        self.payload = {
            "announce": self.user.id,
            "applicant": self.announce.id,
        }

    def test_announce_post_method_unique_success(self):
        res = self.client.post(self.url, self.payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Apply.objects.filter(
                announce=self.user.id,
                applicant=self.announce.id,
            ).exists()
        )

    def test_announce_post_method_duplicate_fail(self):
        # first api post request
        self.client.post(self.url, self.payload)
        # second api post request
        res = self.client.post(self.url, self.payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertRaises(ValidationError)

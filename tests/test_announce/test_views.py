from django.utils.http import urlencode
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from tests.factories import AnnounceFactory, CompanyFactory
from recruit.announce.models import Announcement


def build_url_with_query(viewname: str, *args, **kwargs):
    query_params = kwargs.pop("params", {})
    base_url = reverse(viewname=viewname, *args, **kwargs)
    if query_params:
        base_url += "?" + urlencode(query_params)
    return base_url


class AnnouncementViewSetHTTPTests(TestCase):
    """Test for HTTP methods in ViewSet"""

    def setUp(self):
        self.company_kakao = CompanyFactory.create(name="Kakao")
        self.announce = AnnounceFactory.create(company=self.company_kakao)

        self.url_list = reverse("api:Announce-list")
        self.url_detail = reverse(
            "api:Announce-detail", kwargs={"pk": self.announce.pk}
        )
        self.client = APIClient()

    def test_announce_post_method(self):
        payload = {
            "company": self.company_kakao.id,
            "position": "Backend",
            "credit": 100000,
            "description": "Junior Backend Programmer",
            "technology": "Java",
        }
        res = self.client.post(self.url_list, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(
            Announcement.objects.filter(
                company=self.company_kakao.id,
                position="Backend",
                credit=100000,
            ).exists()
        )

    def test_announce_put_method(self):
        payload = {
            "company": self.company_kakao.id,
            "position": "Backend",
            "credit": 100000,
            "description": "Junior Backend Programmer",
            "technology": "Java",
        }
        res = self.client.put(self.url_detail, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        instance = Announcement.objects.get(id=self.announce.pk)
        for key in payload:
            if key == "company":
                self.assertEqual(getattr(instance, key).id, payload[key])
            else:
                self.assertEqual(getattr(instance, key), payload[key])

    def test_announce_patch_method(self):
        payload = {
            "credit": 500000,
            "technology": "Python",
        }
        res = self.client.patch(self.url_detail, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        for key in payload:
            self.assertEqual(res.data[key], payload[key])

    def test_announce_delete_method(self):
        res = self.client.delete(self.url_detail)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            Announcement.objects.filter(company=self.company_kakao.id).exists()
        )


class AnnouncementViewSetListTests(TestCase):
    """Test for api endpoints for list action in ViewSet"""

    def setUp(self):
        self.announce = AnnounceFactory.create()
        self.url_list = reverse("api:Announce-list")
        self.url_detail = reverse(
            "api:Announce-detail", kwargs={"pk": self.announce.pk}
        )
        self.client = APIClient()

    def test_get_announce_list(self):
        AnnounceFactory.create_batch(4)
        res = self.client.get(self.url_list)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 5)

    def test_search_announce_by_company_name(self):
        wanted_lab = CompanyFactory.create(name="원티드랩")
        wanted_kor = CompanyFactory.create(name="원티드코리아")
        wonder = CompanyFactory.create(name="원더코리아")
        AnnounceFactory.create_batch(3, company=wanted_lab)
        AnnounceFactory.create_batch(4, company=wanted_kor)
        AnnounceFactory.create_batch(4, company=wonder)

        url_wanted = build_url_with_query(
            "api:Announce-list", params={"search": "원티드"}
        )
        res = self.client.get(url_wanted)
        self.assertEqual(len(res.data), 7)

        url_wanted_kor = build_url_with_query(
            "api:Announce-list", params={"search": "원티드코리아"}
        )
        res = self.client.get(url_wanted_kor)
        self.assertEqual(len(res.data), 4)

    def test_search_announce_by_terminology(self):
        AnnounceFactory.create_batch(3, position="Django 백엔드 개발자")
        AnnounceFactory.create_batch(4, technology="django")
        AnnounceFactory.create_batch(
            5, position="Django 백엔드 개발자", technology="Python"
        )
        AnnounceFactory.create_batch(
            6, position="Spring 백엔드 개발자", technology="Java"
        )

        url_django = build_url_with_query(
            "api:Announce-list", params={"search": "Django"}
        )
        res = self.client.get(url_django)
        self.assertEqual(len(res.data), 12)

        url_backend = build_url_with_query(
            "api:Announce-list", params={"search": "백엔드"}
        )
        res = self.client.get(url_backend)
        self.assertEqual(len(res.data), 14)

    def test_get_announce_detail(self):
        res = self.client.get(self.url_detail)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("description", res.data.keys())
        self.assertIn("announce_set", res.data.keys())

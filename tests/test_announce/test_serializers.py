from django.test import TestCase

from tests.factories import AnnounceFactory, CompanyFactory
from recruit.announce.serializers import AnnounceDetailSerializer


class AccountDetailSerializerTests(TestCase):
    """Test for serializer custom method fields"""

    def setUp(self):
        self.company_kakao = CompanyFactory.create(name="Kakao")
        self.announce = AnnounceFactory.create(company=self.company_kakao)
        self.serializer = AnnounceDetailSerializer(instance=self.announce)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "id",
                    "company",
                    "position",
                    "credit",
                    "technology",
                    "description",
                    "announce_set",
                ]
            ),
        )

    def test_company_field_content(self):
        data = self.serializer.data
        self.assertEqual(data["company"]["name"], "Kakao")

    def test_get_announce_set_filter(self):
        company_naver = CompanyFactory.create(name="Naver")
        AnnounceFactory.create_batch(5, company=company_naver)
        data = self.serializer.data
        self.assertEqual(len(data["announce_set"]), 0)

    def test_get_announce_set_listing(self):
        announces_kakao = AnnounceFactory.create_batch(
            5, company=self.company_kakao
        )
        data = self.serializer.data
        self.assertEqual(len(data["announce_set"]), 5)
        self.assertNotIn(self.announce.id, data["announce_set"])

        id_list = [obj.id for obj in announces_kakao]
        self.assertEqual(data["announce_set"], id_list)

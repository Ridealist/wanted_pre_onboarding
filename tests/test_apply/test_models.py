from django.db import IntegrityError
from django.test import TestCase

from recruit.apply.models import Apply
from tests.factories import UserFactory, AnnounceFactory


class ApplyModelTests(TestCase):
    """Test Apply model unique constraint"""

    def setUp(self):
        self.user = UserFactory.create()
        self.annouce = AnnounceFactory.create()
        # instance create
        Apply.objects.create(applicant=self.user, announce=self.annouce)

    def test_apply_unique_constraint(self):
        # duplicate instance fail
        with self.assertRaises(IntegrityError):
            apply_invalid = Apply(applicant=self.user, announce=self.annouce)
            apply_invalid.save()

from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.contrib.auth import get_user_model

from recruit.announce.models import Announcement

User = get_user_model()


class Apply(TimeStampedModel):
    announce = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["announce", "applicant"],
                name="unique_register",
            )
        ]

    def __str__(self):
        return f"{self.announce} - {self.applicant}"

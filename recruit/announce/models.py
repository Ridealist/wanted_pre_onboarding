from django_extensions.db.models import TimeStampedModel
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.constraints import UniqueConstraint

User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    introduce = models.TextField(null=True, blank=True)


class Announcement(TimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    credit = models.IntegerField()
    description = models.TextField()
    technology = models.CharField(max_length=255)


class Register(TimeStampedModel):
    announce = models.ForeignKey(Announcement, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["announce", "applicant"],
                name="unique_register",
            )
        ]

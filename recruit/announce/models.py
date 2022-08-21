from django_extensions.db.models import TimeStampedModel
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    introduce = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Announcement(TimeStampedModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    credit = models.IntegerField()
    description = models.TextField()
    technology = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.company.name} | {self.position} | {self.technology}"

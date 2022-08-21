from django.contrib import admin
from recruit.announce.models import Company, Announcement

admin.site.register([Company, Announcement])

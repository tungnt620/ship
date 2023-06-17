from django.db import models

from . import CompanyStatusType


class Company(models.Model):
    slug = models.SlugField(unique=True, db_index=True)
    name = models.CharField(max_length=255)
    branch_name = models.CharField(
        max_length=255,
        db_comment="With large company, they have different name for "
                   "different products."
    )

    # Below is optional fields
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    logo = models.ImageField(upload_to='company_logos', null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    status = models.CharField(
        max_length=15,
        choices=CompanyStatusType.CHOICES,
        default=CompanyStatusType.ACTIVATED,
    )

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('id',)

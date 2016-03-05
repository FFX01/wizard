from django.db import models
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey


class ContentObject(models.Model):

    title = models.CharField(
        blank=False,
        max_length=120
    )
    slug = models.SlugField(
        blank=True,
        max_length=200
    )
    seo_title = models.CharField(
        blank=True,
        max_length=120
    )
    seo_description = models.CharField(
        blank=True,
        max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(ContentObject, self).save()

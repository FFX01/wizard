from django.db import models
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey


class BaseAbstractContentObject(models.Model):

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

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BaseAbstractContentObject, self).save()


class ContentObject(BaseAbstractContentObject):
    pass


class NestedContentObject(BaseAbstractContentObject, MPTTModel):

    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        abstract = True


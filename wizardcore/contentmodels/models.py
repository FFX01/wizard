from django.db import models
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey


class BaseAbstractContentObject(models.Model):
    """
    All content models inherit from this abstract class. This is a non
    hierarchical model.

    :ivar title: Used for verbose reference, such as in the admin panel.
    :type title: basestring

    :ivar slug: Used for reference or for generating paths.
    :type slug: basestring

    :ivar seo_title: Used for search engine optimization when needed.
    :type seo_title: basestring

    :ivar seo_description: Used for search engine optimization when needed.
    :type seo_description: basestring
    """
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
        """
        Automatically generates a slug if a slug is not defined.

        :param args: Extra positional arguments passed to the save method.

        :param kwargs: Extra keyword arguments passed to the save method.

        :returns Passes the instance back to the original overridden save
        method.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super(BaseAbstractContentObject, self).save()


class ContentObject(BaseAbstractContentObject):
    """
    Basic non-hierarchical content object.
    """
    class Meta:
        abstract = True


class NestedContentObject(BaseAbstractContentObject, MPTTModel):
    """
    Basic hierarchical content object. Used for nested objects.

    :ivar parent: A model instance's parent object. Not required for top level
    model instances.
    :type parent: object
    """

    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        abstract = True


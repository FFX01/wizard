from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from contentmodels.models import NestedContentObject


class BasicPage(NestedContentObject):

    path = models.CharField(
        blank=True,
        max_length=255
    )

    def generate_path(self):
        path = ''
        for obj in self.get_ancestors(include_self=True):
            path += obj.slug + '/'
        return path


@receiver(post_save, sender=BasicPage)
def update_path(sender, instance, **kwargs):
    if not instance.path:
        if instance.parent:
            instance.move_to(instance.parent)
        instance.path = instance.generate_path()
        instance.save()
    elif instance.path:
        new_path = instance.generate_path()
        if instance.path != new_path:
            instance.path = new_path
            instance.save()
        else:
            pass

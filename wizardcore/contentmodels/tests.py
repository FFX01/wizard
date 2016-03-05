from django.test import TestCase
from . import models


class ContentObjectTest(TestCase):

    def test_can_create_content_object(self):

        new_object = models.ContentObject(
            title='Test Object',
            slug='test-object',
            seo_title='Test SEO Title',
            seo_description='Test SEO Description'
        )
        new_object.save()

        object = models.ContentObject.objects.get(slug='test-object')

        self.assertEqual(
            object.seo_title,
            'Test SEO Title',
            msg='Did not retrieve object.'
        )

    def test_content_object_generates_slug(self):

        new_object = models.ContentObject(
            title='New Test Object'
        )
        new_object.save()

        object = models.ContentObject.objects.get(title='New Test Object')

        self.assertEqual(
            object.slug,
            'new-test-object'
        )


class NestedContentObjectTest(TestCase):

    def test_can_create_object(self):

        new_model = models.NestedContentObject(
            title='Nested Content Test',
            slug='nested-content-test'
        )

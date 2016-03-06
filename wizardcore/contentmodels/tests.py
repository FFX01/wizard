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

        model = models.ContentObject.objects.get(slug='test-object')

        self.assertEqual(
            model.title,
            'Test Object'
        )
        self.assertEqual(
            model.seo_title,
            'Test SEO Title',
            msg='Did not retrieve object.'
        )
        self.assertEqual(
            model.seo_description,
            'Test SEO Description'
        )

    def test_content_object_generates_slug(self):

        new_object = models.ContentObject(
            title='New Test Object'
        )
        new_object.save()

        model = models.ContentObject.objects.get(title='New Test Object')

        self.assertEqual(
            model.slug,
            'new-test-object'
        )


class NestedContentObjectTest(TestCase):

    def test_can_create_object(self):

        new_model = models.NestedContentObject(
            title='Nested Content Test',
            slug='nested-content-test',
            seo_title='Nested Content Object SEO Title',
            seo_description='Nested Content Object SEO description.'
        )
        new_model.save()

        model = models.NestedContentObject.objects.get(slug='nested-content-test')

        self.assertEqual(
            model.title,
            'Nested Content Test'
        )
        self.assertEqual(
            model.seo_title,
            'Nested Content Object SEO Title'
        )
        self.assertEqual(
            model.seo_description,
            'Nested Content Object SEO description.'
        )

    def test_nested_content_object_generates_slug(self):

        new_object = models.NestedContentObject(
            title='New Test Object'
        )
        new_object.save()

        model = models.NestedContentObject.objects.get(title='New Test Object')

        self.assertEqual(
            model.slug,
            'new-test-object'
        )

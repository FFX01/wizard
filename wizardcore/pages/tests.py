from django.test import TestCase
from .models import BasicPage


class BasicPageTest(TestCase):

    def test_can_create_basic_page(self):

        new_page = BasicPage(
            title='Test Basic Page',
            slug='test-basic-page',
            seo_title='Test SEO Title',
            seo_description='Test SEO description',
            parent=None
        )
        new_page.save()

        page = BasicPage.objects.get(slug='test-basic-page')

        self.assertEqual(
            page.title,
            'Test Basic Page',
            msg='Fetched Basic Page instance did not return correct title.'
        )

        self.assertEqual(
            page.seo_title,
            'Test SEO Title',
            msg='Fetched Basic Page instance did not return correct SEO Title.'
        )

        self.assertEqual(
            page.seo_description,
            'Test SEO description',
            msg='Fetched Basic Page instance did not return correct SEO Description.'
        )

        self.assertEqual(
            page.parent,
            None,
            msg='Fetched Basic Page returned a parent when it does not have one.'
        )

    def test_basic_page_can_have_parent(self):

        top_level_page = BasicPage(
            title='Top Level Page',
            slug='top-level-page',
            seo_title='SEO Title',
            seo_description='SEO description',
            parent=None
        )
        top_level_page.save()

        nested_page = BasicPage(
            title='Nested Page',
            slug='nested-page',
            seo_title='SEO Title',
            seo_description='SEO description',
            parent=BasicPage.objects.get(slug='top-level-page')
        )
        nested_page.save()

        parent_page = BasicPage.objects.get(slug='top-level-page')
        child_page = BasicPage.objects.get(slug='nested-page')

        self.assertEqual(
            child_page.parent,
            parent_page
        )

    def test_basic_page_generates_path(self):

        new_page = BasicPage(
            title='Test Page Path',
            slug='test-page-path',
            parent=None
        )
        new_page.save()

        page = BasicPage.objects.get(slug='test-page-path')

        self.assertTrue(
            page.path,
            msg='Saving Basic Page instance did not create correct path.'
        )

    def test_nested_basic_page_generates_path(self):

        top_level_page = BasicPage(
            title='Top Level Page 2',
            slug='top-level-page-2',
            parent=None
        )
        top_level_page.save()

        nested_page = BasicPage(
            title='Nested Page 2',
            slug='nested-page-2',
            parent=BasicPage.objects.get(slug='top-level-page-2')
        )
        nested_page.save()

        page = BasicPage.objects.get(slug='nested-page-2')

        self.assertTrue(
            page.path,
            msg='Basic Page instance did not generate path on save.'
        )

        self.assertEqual(
            page.path,
            'top-level-page-2/nested-page-2/',
            msg='Basic Page instance did not generate correct path on save.'
        )

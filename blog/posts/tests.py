from django import test
from django.contrib import admin as django_admin
from django.db import models as django_models

from blog.posts import models


class PostTestCase(test.TestCase):
    model = models.Post

    def assert_has_field(self, name):
        self.assertIn(name, self.model._meta.get_all_field_names())

    def _field(self, name):
        return self.model._meta.get_field_by_name(name)[0]

    def test_should_have_title(self):
        self.assert_has_field("title")

    def test_title_should_be_CharField(self):
        self.assertIsInstance(self._field("title"), django_models.CharField)

    def test_title_should_have_at_most_500_characters(self):
        self.assertEqual(500, self._field("title").max_length)

    def test_should_have_body(self):
        self.assert_has_field("body")

    def test_body_should_be_a_TextField(self):
        self.assertIsInstance(self._field("body"), django_models.TextField)


class PostAdminTestCase(test.TestCase):

    def test_Post_is_registered_within_django_admin(self):
        django_admin.autodiscover()
        self.assertIn(models.Post, django_admin.site._registry)

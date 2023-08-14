#coding:utf-8

from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory

# Create your tests here.
from snippets.models import Snippet
from django.urls import resolve
from snippets.views import top, snippet_new, snippet_edit, snippet_detail


class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        found = resolve("/snippets/new/")
        self.assertEqual(snippet_new, found.func)


class SnippetDetailTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve("/snippets/1/")
        self.assertEqual(snippet_detail, found.func)


class EditSnippets(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit, found.func)

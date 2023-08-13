#coding:utf-8

from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory

# Create your tests here.
from snippets.models import Snippet
from snippets.views import top

UserModel = get_user_model()


class TopPageRenderSnippetsTest(TestCase):
    def setup(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass0001",
        )

        self.snippet = Snippet.objects.create(
            title="title",
            code="print('Hello World')",
            description="description1",
            created_by=self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)

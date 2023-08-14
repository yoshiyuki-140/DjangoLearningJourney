#coding:utf-8

# This test
from django.contrib.auth import get_user_model
from django.test import TestCase, Client, RequestFactory
from snippets.models import Snippet
from django.urls import resolve
from snippets.views import top, snippet_new, snippet_edit, snippet_detail


# class CreateSnippetTest(TestCase):
#     def test_should_resolve_snippet_new(self):
#         found = resolve("/snippets/new/")
#         self.assertEqual(snippet_new, found.func)

UserModel = get_user_model()

class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="secret",
        )

        self.snippet = Snippet.objects.create(
            title="タイトル",
            code="コード",
            description="解説",
            created_by=self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(response, "snippets/snippet_detail.html")

    def test_top_page_returns_200_and_expected_heading(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertContains(response, self.snippet.title, status_code=200)

    # def test_should_resolve_snippet_detail(self):
    #     found = resolve("/snippets/1/")
    #     self.assertEqual(snippet_detail, found.func)


# class EditSnippets(TestCase):
#     def test_should_resolve_snippet_edit(self):
#         found = resolve("/snippets/1/edit/")
#         self.assertEqual(snippet_edit, found.func)

# This test

# class TopPageRendrSnippetsTest(TestCase):
#     def setUp(self):
#         self.user = UserModel.objects.create(
#             username="test_user",
#             email="test@example.com",
#             password="top_secret_pass0001"
#         )
# 
#         self.snippet = Snippet.objects.create(
#             title="title1",
#             code="print('hello')",
#             description="description1",
#             created_by=self.user,
#         )
# 
#     def test_should_return_snippet_title(self):
#         request = RequestFactory().get("/")
#         request.user = self.user
#         response = top(request)
#         self.assertContains(response, self.snippet.title)
# 
#     def test_should_return_username(self):
#         request = RequestFactory().get("/")
#         request.user = self.user
#         response = top(request)
#         self.assertContains(response, self.user.username)

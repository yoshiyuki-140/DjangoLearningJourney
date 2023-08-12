#coding:utf-8

from django.test import TestCase

# Create your tests here.
from django.http import HttpRequest

# 波線でるけど、テストコードとして実行するときはmanage.pyがある所から実行されるんで正しいコードだぞ
from snippets.views import top


# class TopPageViewTest(TestCase):
    # def test_top_returns_200(self):
        # request = HttpRequest()  # リクエストオブジェクトの作成
        # response = top(request)
        # self.assertEqual(response.status_code, 200)
# 
    # def test_top_returns_expected_content(self):
        # request = HttpRequest()  # httpオブジェクトの作成
        # response = top(request)
        # self.assertEqual(response.content, b"Hello World")


class TopPageTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")

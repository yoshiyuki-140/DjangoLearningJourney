
# Create your views here.
from snippets.models import Snippet
from django.shortcuts import render


def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}  # テンプレートエンジンに与えるpythonオブジェクト
    return render(request, "snippets/top.html", context)

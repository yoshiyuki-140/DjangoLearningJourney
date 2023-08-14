
# Create your views here.
from snippets.models import Snippet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def top(request):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}  # テンプレートエンジンに与えるpythonオブジェクト
    return render(request, "snippets/top.html", context)


def snippet_new(request):
    return HttpResponse('スニペットの登録')


def snippet_edit(request, snippet_id):
    return HttpResponse('スニペットの編集')


def snippet_detail(request, snippet_id):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, "snippets/snippet_detail.html", {'snippet': snippet})

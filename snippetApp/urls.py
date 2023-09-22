from django.urls import path

from snippetApp.views import snippet_new, snippet_edit, snippet_detail

urlpatterns = [
    path('new/', snippet_new, name='snippet_new'),
    path('<int:snippet_id>/', snippet_edit, name='snippet_edit'),
    path('<int:snippet_id>/', snippet_detail, name='snippet_detail')
]

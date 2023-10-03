# viewの役割に関して

- ユーザーからのリクエストを受け取り,それに基づいたレスポンスを生成するコンポーネント.

- urlを決めるのはurls.pyのurlpattern(list object)

templateの指定はviewで行う -> クラスベースビューだと
```python
{viewname}.as_view(template_name="template file location path")
```
という指定方法で書くことができる.

- path関数のname引数はテンプレートの中でリンクを張るときに使う.
例えば
```python

from django.urls import 
from django.auth.views import LoginView,TemplateView
from views import top
urlpattern = [
    path('accounts/login/',LoginView.as_view(template_name='accounts/login.html'),name="login"),
    path('accounts/top/',TemplateView.as_view(template_name='accounts/top.html'),name="top"),
]
```
と定義されている場合,
top.htmlの中では

top.html
```html
{% extends "base.html" %}
{% load django_bootstrap5 %}

{% block main %}
<h1>this is login link</h1>
<a link="{% url 'login' %}">LOGIN</a>
{% endblock main %}
```
と書けばアンカータグにlogin.htmlへのリンクが挿入される


## settings.pyに関して
- DIRSはリスト形式でtemplateの探し先パスを書く
- APP_DIRSはブール型の値を挿入する,Trueの時は各アプリケーション配下のtemplatesディレクトリが参照される.
- ファイル名が同じ場合は,djangoはINSTALLED_APPSに記述された中で上から順番で各アプリケーション配下のtemplatesを参照する.
最初に見つかったものを参照する.(おそらく見つかった時点で参照を終了するからそうなる)

## コンテキストプロセッサーとは
djangoのテンプレートにコンテキストを与える方法はviewのrender関数の引数にcontextを渡す方法があった.
しかしながら,これ以外にもコンテキストを渡すことは可能である.
それが、コンテキストプロセッサーである.
例えば、表示しようとしているすべてのテンプレートにおいて特定のコンテキストが必要な場合は,コンテキストプロセッサーに登録しておけば,毎度毎度viewを書くときに引数に書く手間を省くことができる.
> CSRFトークンは自動で使用できるコンテキストであるが,settings.pyのコンテキストプロセッサーオプションには含まれていなくて、無効化できない.

## テンプレートフィルターとは
- テンプレート内で変数を加工して表示することができる.

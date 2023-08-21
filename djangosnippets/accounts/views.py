from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.


# フォームクラスを使用した登録処理の流れ

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        # POSTリクエストを受け取ったら form.is_validメソッドと form.saveメソッドを呼ぶ

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(...)

    else:
        # GET リクエストを受け取ったらformオブジェクトを用紙して、テンプレートで表示
        form = UserCreationForm()

    return render(request, "signup.html", {'form': form})

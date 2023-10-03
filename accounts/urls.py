from django.urls import path
from .views import SignupView
from django.contrib.auth.views import *

signup_view = SignupView.as_view(template_name='accounts/signup.html')
login_view = LoginView.as_view(template_name='accounts/login.html')
logout_view = LogoutView.as_view(template_name='accounts/logout.html')
password_change_view = PasswordChangeView.as_view(template_name='accounts/password_change.html')
password_change_done_view = PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html')
password_reset_view = PasswordResetView.as_view(template_name='accounts/password_reset.html')
password_reset_done_view = PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html')
password_reset_confirm_view = PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html')
password_reset_complete_view = PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html')

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),
    path('password_change/', password_change_view, name='password_change'),
    path('password_change/done/', password_change_done_view,name='password_change_done'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('password_reset/done/', password_reset_done_view, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete_view,name='password_reset_complete'),
]
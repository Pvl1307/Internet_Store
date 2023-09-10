from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, ConfirmEmailView, VerifyEmailView, \
    ConfirmationSuccessView, ConfirmationErrorView, GenerateAndSendPasswordView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/verify_email/', VerifyEmailView.as_view(), name='verify_email'),
    path('confirm_email/<str:token>/', ConfirmEmailView.as_view(), name='confirm_email'),


    path('confirmation_success/', ConfirmationSuccessView.as_view(), name='confirmation_success'),
    path('confirmation_error/', ConfirmationErrorView.as_view(), name='confirmation_error'),


    path('generate_send_password/', GenerateAndSendPasswordView.as_view(), name='generate_send_password'),
]

from django.urls import path, include
from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserRefreshView, UserChangePasswordView, SendPasswordResetEmailView, UserPasswordResetView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('me/', UserProfileView.as_view(), name='me'),
    path('refresh/', UserRefreshView.as_view(), name='refresh'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',
         UserPasswordResetView.as_view(), name='reset-password'),

]

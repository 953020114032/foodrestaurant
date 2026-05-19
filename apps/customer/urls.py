from django.urls import path
from .views import SendOTPView,CustomerRegisterView,VerifyOTPView

urlpatterns = [
    path("otp/",SendOTPView.as_view()),
    path("otp-verify/",VerifyOTPView.as_view()),
    path("customer/register/",CustomerRegisterView.as_view())
]

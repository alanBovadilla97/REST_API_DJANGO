from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage),
    path("accounts/", views.BankAccountList.as_view()),
    path("accounts/<int:pk>", views.BankAccountDetail.as_view())
]
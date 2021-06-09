from rest_framework import generics
from .models import BankAccount
from .serializers import BankAccountSerializer
from django.shortcuts import render

# Create your views here.

def HomePage(request):
    return render(request, 'homePage.html')

class BankAccountList(generics.ListCreateAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class BankAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

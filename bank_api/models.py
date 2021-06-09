from django.db import models

class BankAccount(models.Model):
    ownerName = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    accountType =models.CharField(max_length=255)

    def __str__(self):
        return self.ownerName + " " + self.accountType
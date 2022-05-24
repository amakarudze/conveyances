from django.db import models
from django.contrib.auth import get_user_model


class Bank(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ConveyanceMatter(models.Model):
    title = models.CharField(max_length=255)
    matters = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

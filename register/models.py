from django.db import models
from django.contrib.auth.models import User

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="developer_profile")
    experience = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.user.username

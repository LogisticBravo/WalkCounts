from django.contrib.auth.models import User
from django.db import models
from steps.models import Goals
# # Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.OneToOneField(Goals, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"{self.user}"

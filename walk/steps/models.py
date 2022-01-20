from django.db import models
from django.contrib.auth.models import User


class Target(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True)
    goal = models.IntegerField(null=True)
    goal_submitted = models.DateTimeField('goal submitted', null=True)
    steps = models.IntegerField(null=True, default=0)

    def __str__(self):
        return f"{self.user}, {self.goal}, {self.steps}"

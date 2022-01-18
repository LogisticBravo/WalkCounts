from django.db import models


# Create your models here.
class Goals(models.Model):
    goals = models.IntegerField()
    submit_date = models.DateTimeField('date submitted')
    first_name = models.CharField(max_length=255)
    user = models.EmailField()

    class Meta:
        verbose_name_plural = "Goals"

    def __str__(self):
        return f"{self.goals}, {self.submit_date}, {self.first_name}, {self.user}"


class Steps(models.Model):
    steps = models.IntegerField()
    submit_date = models.DateTimeField('date submitted')
    first_name = models.CharField(max_length=255)
    user = models.EmailField()

    class Meta:
        verbose_name_plural = "Steps"

    def __str__(self):
        return f"{self.steps}, {self.submit_date}, {self.first_name}, {self.user}"

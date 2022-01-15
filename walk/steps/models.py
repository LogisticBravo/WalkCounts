from django.db import models


# Create your models here.
class Goals(models.Model):
    goals = models.IntegerField()
    submit_date = models.DateTimeField('date submitted')

    class Meta:
        verbose_name_plural = "Goals"

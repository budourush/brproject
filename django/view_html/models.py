from django.db import models


# Create your models here.

class SampleModel(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id

from django.db import models

# Create your models here.

class Food(models.Model):

    fname=models.CharField(max_length=200)

    price=models.PositiveIntegerField()


    def __str__(self):

        return self.fname

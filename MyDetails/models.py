from django.db import models

# Create your models here.


class MyDetails(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname + " "+self.lastname

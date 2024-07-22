from django.db import models

# Create your models here.
class Store(models.Model):
    Firstname=models.CharField("enter your first name",max_length=100)
    Lastname=models.CharField("enter you last name",max_length=100)
    contact=models.IntegerField(("enter your number"))
    Email=models.EmailField(("enter your email"), max_length=254)
    
    def __str__(self) -> str:
        return self.Firstname+" "+self.Lastname

class Hello(models.Model):
    name=models.CharField("enter your petname:",max_length=100)
    pettype=models.CharField("enter like dog or cat or pig:",max_length=100)
    def __str__(self):
        return self.name
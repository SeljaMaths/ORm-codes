from django.db import models

# Create your models here.


class register(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    age = models.IntegerField()


class product(models.Model):
    product_name = models.CharField(max_length=200)

    Rate = models.IntegerField()
    customer = models.ForeignKey(register,on_delete=models.CASCADE)




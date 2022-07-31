from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.TextField(max_length=200)
    price = models.FloatField(default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )

    def __str__(self) -> str:
        return self.name

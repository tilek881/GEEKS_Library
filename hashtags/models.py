from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, related_name='products')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

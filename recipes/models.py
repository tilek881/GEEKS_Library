from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    GRAMS = 'граммы'
    KILOGRAMS = 'килограммы'
    MILLILITERS = 'миллилитры'
    LITERS = 'литры'
    PIECES = 'штуки'

    UNIT_CHOICES = [
        (GRAMS, 'Граммы'),
        (KILOGRAMS, 'Килограммы'),
        (MILLILITERS, 'Миллилитры'),
        (LITERS, 'Литры'),
        (PIECES, 'Штуки'),
    ]

    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default=GRAMS)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"

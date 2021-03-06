from django.db import models

# Create models from bride no zilla.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    inventory_id = models.ForeignKey(
        'Inventory', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    class Meta:
        verbose_name_plural = "Inventories"

    name = models.CharField(max_length=254)
    quantity = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name


# class Review(models.Model):
#     title = models.CharField(max_length=254)
#     description = models.TextField()
#     rating = models.DecimalField(
#         max_digits=6, decimal_places=2, null=True, blank=True)

#     def __str__(self):
#         return self.title

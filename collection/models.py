from django.db import models

class Shirt(models.Model):
    shirt_name = models.CharField(max_length=100)
    shirt_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='collection/Image/Shirt/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shirt_name

class Pant(models.Model):
    pant_name = models.CharField(max_length=100)
    pant_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='collection/Image/Pant/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pant_name

class Shoe(models.Model):
    shoe_name = models.CharField(max_length=100)
    shoe_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='collection/Image/Shoe/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shoe_name

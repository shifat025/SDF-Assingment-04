from django.db import models

# Create your models here.

class category_model(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name
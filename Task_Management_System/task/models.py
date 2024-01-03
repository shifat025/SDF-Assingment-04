from django.db import models
from category.models import category_model

# Create your models here.

class task_model(models.Model):
    task_title = models.CharField(max_length=250)
    task_description = models.TextField()
    task_assign_date = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(category_model)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_title
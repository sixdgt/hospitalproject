from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100)
    category_code = models.CharField(max_length=10)

    class Meta:
        db_table = "app_categories"

class Hospital(models.Model):
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    contact = models.IntegerField()
    added_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = "app_hospitals"

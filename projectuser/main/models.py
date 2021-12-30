from enum import unique
from django.db import models

# Create your models here.
class ProductUser(models.Model):

    # id = models.IntegerField()
    user_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        unique_together=('user_id', 'product_id')
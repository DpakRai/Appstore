from django.db import models
from users import models as user_model

# Create your models here.
class payments(models.Model):
    user_id= models.ForeignKey(user_model.User,on_delete=models.CASCADE)
    payment_name = models.CharField(max_length=100)
    payment_type = models.CharField(max_length=100)
    payment_amount= models.PositiveIntegerField()


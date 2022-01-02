from django.db import models
from users import models as user_model

class subscriptions(models.Model):
    user_id= models.ForeignKey(user_model.User,on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=100)
    sub_type = models.CharField(max_length=100)
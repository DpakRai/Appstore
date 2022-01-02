from django.db import models
from users import models as user_model

# Create your models here.
class extension(models.Model):
    user_id= models.ForeignKey(user_model.User,on_delete=models.CASCADE)

    title = models.CharField(max_length=100, primary_key=True)
    cover = models.CharField(max_length=100)
    description_extinsion = models.CharField(max_length=250)
    developer = models.CharField(max_length=250)
    rating = models.CharField(max_length=100)
    download = models.CharField(max_length=100)
    screenshots= models.ImageField()
    review= models.CharField(max_length=100)
    demo = models.ImageField()

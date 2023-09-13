from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipes(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name=models.CharField(max_length=200, null=False)
    recipe_description= models.TextField()
    recipe_image= models.ImageField(upload_to="recipe_assets")

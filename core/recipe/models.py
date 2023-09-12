from django.db import models

# Create your models here.

class Recipes(models.Model):
    recipe_name=models.CharField(max_length=200, null=False)
    recipe_description= models.TextField()
    recipe_image= models.ImageField(upload_to="recipe_assets")

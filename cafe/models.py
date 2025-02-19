from django.db import models
from django.conf import settings

# Create your models here.
class Cafe(models.Model):
    cafename=models.CharField(max_length=20)
    cafelocations=models.CharField(max_length=100)
    cafeinfo=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.cafename
    
class CafeImage(models.Model):
    cafe=models.ForeignKey(Cafe, null=True, blank=True, on_delete=models.CASCADE)
    cafeimage=models.ImageField(blank=True, upload_to="cafeimage/", default='cafe_default_image.png')
    
    def __str__(self):
        return f"Image for post {self.cafe.id}"
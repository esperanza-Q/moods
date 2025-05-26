from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    code = models.CharField(max_length=30, unique=True)  # ex: "coffee", "study"
    label = models.CharField(max_length=50)  # ex: "#커피가 맛있는"


class Cafe(models.Model):
    cafename=models.CharField(max_length=20)
    cafelocations=models.CharField(max_length=100)
    cafeinfo=models.CharField(max_length=50)
    cafeID=models.IntegerField(null=False, default=0)
    cafe_x=models.FloatField(max_length=50, null=False, default=0.0)
    cafe_y=models.FloatField(max_length=50, null=False, default=0.0)
    cafe_most_tags = models.ManyToManyField(Tag, related_name='featured_in', blank=True)

    def __str__(self):
        return self.cafename
    
class CafeImage(models.Model):
    cafe=models.ForeignKey(Cafe, null=True, blank=True, on_delete=models.CASCADE)
    cafeimage=models.ImageField(blank=True, upload_to="cafeimage/", default='cafe_default_image.png')
    
    def __str__(self):
        return f"Image for post {self.cafe.id}"
    


from django.db import models
from cafe.models import Cafe
from django.contrib.auth.models import User


# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    review_image=models.ImageField(blank=True, upload_to="review_images/")
    review_content=models.TextField()
    
    def __str__(self):
        return self.review_content[:50]
    
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('guest', 'Guest'),  # 인증 전 유저
        ('verified', 'Verified User'),  # 인증된 유저
    )
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nickname=models.CharField(max_length=20)
    profile_image=models.ImageField(blank=True, upload_to="image/", default='default.jpeg')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='guest')
    
    def __str__(self):
        return self.nickname
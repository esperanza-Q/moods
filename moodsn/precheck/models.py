from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from accounts.models import Profile

# Create your models here.
class Checkpost(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content=models.TextField()
    # verified_check=models.BooleanField(default=False)
    verified_check = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    @property
    def verified_user_type(self):
        return self.verified_check.user_type
    

    
class CheckImage(models.Model):
    checkpost=models.ForeignKey(Checkpost, null=True, blank=True, on_delete=models.CASCADE)
    checkimage = models.ImageField(upload_to='check_images/', null=True, blank=True)
    
    def __str__(self):
        return f"Image for post {self.checkpost.id}"
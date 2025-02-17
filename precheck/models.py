from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Checkpost(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    content=models.TextField()
    
    def __str__(self):
        return self.user.username
    
    # def save(self, *args, **kwargs):
    #     # 유저가 이미 checkpost를 작성한 경우 예외 발생
    #     if checkpost.objects.filter(user=self.user).exists():
    #         raise ValidationError("한 유저는 하나의 인증글만 작성할 수 있습니다.")
    #     super().save(*args, **kwargs)
    
class CheckImage(models.Model):
    checkpost=models.ForeignKey(Checkpost, null=True, blank=True, on_delete=models.CASCADE)
    checkimage = models.ImageField(upload_to='check_images/', null=True, blank=True)
    
    def __str__(self):
        return f"Image for post {self.checkpost.id}"
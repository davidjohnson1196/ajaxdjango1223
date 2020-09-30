from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    post_heading=models.CharField(max_length=200)
    post_text=models.TextField()

    def __str__(self):
        return self.post_heading


class Like(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    likedby=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} liked by {self.likedby}'

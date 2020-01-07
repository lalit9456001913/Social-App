from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


from django.contrib.auth.models import User
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes=models.IntegerField()
    dislikes=models.IntegerField()

class Liked(models.Model):
    like_id=models.AutoField(primary_key=True)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)


class Dislike(models.Model):
    dislike_id=models.AutoField(primary_key=True)
    post_id=models.ForeignKey(Post,on_delete=models.CASCADE)
    user_id=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)





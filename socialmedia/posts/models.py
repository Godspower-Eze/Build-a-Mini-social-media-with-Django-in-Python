from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Posts(models.Model):
    class Meta:
        verbose_name_plural = 'Posts'

    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    time_posted = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default="default.jpg", upload_to='post_pics')

    def __str__(self):
        return f'{self.post_title} {self.id}'

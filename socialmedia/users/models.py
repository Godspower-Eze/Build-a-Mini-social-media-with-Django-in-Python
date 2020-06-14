from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from PIL import Image

gender = (
    ('', ''),
    ('male', 'Male'),
    ('female', 'Female')
)

size = (300, 300)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='related user')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=gender, default=gender[0][0])
    picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio_data = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.picture.path)
        image.thumbnail(size)
        image.save(self.picture.path)

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user = Profile(user=instance, first_name=User.objects.get(id=instance.id).username)
            user.save()

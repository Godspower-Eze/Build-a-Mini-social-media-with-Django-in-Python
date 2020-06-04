from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

gender = (
    ('', ''),
    ('male', 'Male'),
    ('female', 'Female')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=gender, default=gender[0][0])
    picture = models.ImageField()

    def __str__(self):
        return f"{self.user.username} {self.id}"

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user = Profile(user=instance, first_name=User.objects.get(id=instance.id).username)
            user.save()

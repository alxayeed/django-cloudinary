from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    profile_image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name

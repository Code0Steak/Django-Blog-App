from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #if the User is deleted the profile for the user will be gone. But not viceversa.
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'Profile for {self.user.username}'
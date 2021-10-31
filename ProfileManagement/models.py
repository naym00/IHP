from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileInformation(models.Model):
    nickname = models.CharField(max_length=20 , null=True)
    profilepic = models.ImageField(upload_to='images/profilepic/',  blank=True, null=True)
    coverpic = models.ImageField(upload_to='images/coverpic/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
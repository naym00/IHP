from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EncodedData(models.Model):
    Starting_Index = models.IntegerField(blank=True, null=True)
    Ghap = models.IntegerField(blank=True, null=True)
    Add_a_Value = models.IntegerField(blank=True, null=True)
    HiddenData = models.TextField(blank=True, null=True)
    LengthOfString = models.IntegerField(blank=True, null=True)
    SavingPath = models.CharField(max_length=500,  blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

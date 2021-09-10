from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Shoe(models.Model):
    Size_Choices =(
    ("4", "4"),
    ("4.5", "4.5"),
    ("5", "5"),
    ("5.5", "5.5"),
    ("6", "6"),
    ("6.5", "6.5"),
    ("7", "7"),
    ("7.5", "7.5"),
    ("8", "8"),
    ("8.5", "8.5"),
    ("9", "9"),
    ("8.5", "9.5"),
    ("9.5", "8.5"),
    ("10", "10"),
    ("10.5", "10.5"),
    ("11", "11"),
    ("11.5", "11.5"),
    ("12", "12"),
    ("12.5", "12.5"),
)

    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    size = models.CharField(max_length=20 ,choices=Size_Choices, default= '6' )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={'shoe_id': self.id})


class Photo(models.Model):
  url = models.CharField(max_length=250)
  shoe = models.OneToOneField(Shoe, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for shoe_id: {self.shoe_id} @{self.url}"
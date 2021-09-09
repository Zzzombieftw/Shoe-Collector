from django.db import models

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
    ("11", "1"),
    ("11.5", "11.5"),
    ("12", "12"),
    ("12.5", "12.5"),
)

    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    colorway = models.CharField(max_length=100)
    size = models.CharField(max_length=20 ,choices=Size_Choices, default= '4' )

    def __str__(self):
        return self.name
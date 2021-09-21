from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=20)
    shorthand=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    name=models.CharField(max_length=20)
    country=models.ForeignKey("Country",on_delete=models.CASCADE)
    shorthand=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class City(models.Model):
    name=models.CharField(max_length=50)
    state=models.ForeignKey("State",on_delete=models.CASCADE)
    shorthand=models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name
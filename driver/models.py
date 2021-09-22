from django.db import models
from django.db.models.fields import DateTimeField
# Create your models here.
class DriverTrip(models.Model):
    Starting_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='start_city')
    Destination_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='end_city')
    Trip_Starting_Time=models.DateTimeField()
    Trip_Ending_Time=models.DateTimeField()
    isTripStarted=models.BooleanField(default=False)
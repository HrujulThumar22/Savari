from django.db import models
from django.db.models.fields import DateTimeField
# Create your models here.
class DriverTrip(models.Model):
    Starting_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='start_city')
    Destination_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='end_city')
    Trip_Starting_Date=models.DateField()
    Trip_Starting_Time=models.TimeField()
    Trip_Ending_Date=models.DateField()
    Trip_Ending_Time=models.TimeField()
    Driver=models.ForeignKey("userAccount.User", on_delete=models.CASCADE)
    isTripStarted=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Driver.username+':'+self.Starting_City.name+'-'+self.Destination_City.name
from django.db import models
from django.db.models.fields import DateTimeField
from django.core.validators import RegexValidator
# Create your models here.
class stop(models.Model):
    addstop=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='stop_city')
    tmpstop=models.CharField(max_length=255)
class DriverTrip(models.Model):
    Starting_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='start_city')
    Destination_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='end_city')
    Trip_Starting_Date=models.DateField()
    Trip_Starting_Time=models.TimeField()
    Trip_Ending_Date=models.DateField()
    Trip_Ending_Time=models.TimeField()
    Stops=models.ForeignKey("stop.tmpstop",on_delete=models.CASCADE,related_name='all_stop')
    Vehicle_Name=models.CharField(max_length=50)
    number_regex=RegexValidator(regex=r'^[A-Z]{2}[-][0-9]{1,2}[-][A-Z]{1,2}[-][0-9]{3,4}$', message="Vehicle number must be entered in the format: MH-03-C-3843")
    Vehicle_Number=models.CharField(validators=[number_regex], max_length=17, blank=True)
    Vacancy=models.IntegerField()
    Driver=models.ForeignKey("userAccount.User", on_delete=models.CASCADE)
    isTripStarted=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Driver.username+':'+self.Starting_City.name+'-'+self.Destination_City.name
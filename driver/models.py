from django.db import models
from django.db.models.fields import DateTimeField
from django.core.validators import RegexValidator
# Create your models here.
class DriverTrip(models.Model):
    STATUS_CHOICES =(
        ("0", "Not Started"),
        ("1", "Started"),
        ("2", "Ended"),
    )
    Starting_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='start_city')
    Destination_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='end_city')
    Trip_Created_On=models.DateTimeField(auto_now_add=True)
    Stops=models.CharField(max_length=255)
    Vehicle_Name=models.CharField(max_length=50)
    number_regex=RegexValidator(regex=r'^[A-Z]{2}[-][0-9]{1,2}[-][A-Z]{1,2}[-][0-9]{3,4}$', message="Vehicle number must be entered in the format: MH-03-C-3843")
    Vehicle_Number=models.CharField(validators=[number_regex], max_length=17, blank=True)
    Vacancy=models.IntegerField()
    Driver=models.ForeignKey("userAccount.User", on_delete=models.CASCADE)
    TripStatus=models.CharField(max_length=1,choices=STATUS_CHOICES,default=0,)
    #vehical image
    def __str__(self) -> str:
        return self.Driver.username+':'+self.Starting_City.name+'-'+self.Destination_City.name
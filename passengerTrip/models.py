from django.db import models

# Create your models here.

class UserTrip(models.Model):
    STATUS_CHOICES =(
        ("0", "Unattended"),
        ("1", "Accepted"),
        ("2", "Rejected"),
    )
    passenger=models.ForeignKey('userAccount.User',on_delete=models.CASCADE)
    trip=models.ForeignKey('driver.driverTrip',on_delete=models.CASCADE)
    noOfSeatsBooked=models.IntegerField()
    requestStatus=models.CharField(max_length=1,choices=STATUS_CHOICES,default=0,)
    tripBookedOn=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.passenger.username+': '+str(self.trip.id)

class BookRide(models.Model):
    Starting_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='starting_city')
    Destination_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='ending_city')
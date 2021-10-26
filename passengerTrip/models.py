from django.db import models

# Create your models here.

class UserTrip(models.Model):
    passenger=models.ForeignKey('userAccount.User',on_delete=models.CASCADE)
    trip=models.ForeignKey('driver.driverTrip',on_delete=models.CASCADE)
    noOfSeatsBooked=models.IntegerField()
    isTripComfirmed=models.BooleanField(default=False)
    tripBookedOn=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.passenger.username+': '+str(self.trip.id)

class BookRide(models.Model):
    Starting_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='starting_city')
    Destination_City=models.ForeignKey("city.City",on_delete=models.CASCADE,related_name='ending_city')
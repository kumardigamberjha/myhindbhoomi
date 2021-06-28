from django.db import models
from django.utils.timezone import timezone

class Messages(models.Model):
    email = models.CharField(max_length=150, default="", null=True)
    message = models.CharField(max_length=150, default="", null=True)

    def __str__(self):
        return self.email

class Train_Btw_Station(models.Model):
    Train_No = models.IntegerField()
    Train_Name = models.CharField(max_length= 300)
    Source_Station_Name = models.CharField(max_length= 300)
    Destination_Station_Name = models.CharField(max_length= 300)
    days = models.CharField(max_length=50)
    sleeper = models.IntegerField(default=0,blank=True, null=True)
    AC1 = models.IntegerField(default=0,blank=True, null=True)
    AC2 = models.IntegerField(default=0,blank=True, null=True)
    AC3 = models.IntegerField(default=0,blank=True, null=True)
    general = models.IntegerField(default=0,blank=True, null=True)
    date1 = models.DateTimeField(auto_now=True)
    qry_date = models.DateTimeField()

    def __str__(self):
        return self.Train_Name
    
class myTrains(models.Model):
    train_number = models.IntegerField(default=0,blank=True, null=True)
    arrival = models.TimeField()
    day = models.CharField(max_length=50)
    train_name = models.CharField(max_length=300)
    Source_Station_Name = models.CharField(max_length= 300)
    Destination_Station_Name = models.CharField(max_length= 300)
    departure = models.TimeField()
    
    def __str__(self):
        return self.train_name

class state(models.Model):
    name = models.CharField(max_length=100, default = "")
    capital = models.CharField(max_length=100,blank=True, default = "", null=True)
    history = models.TextField(default="",blank=True, null=True)
    img1 = models.ImageField(default="",blank=True, null=True)
    imag2 = models.ImageField(default="",blank=True, null=True)
    imag3 = models.ImageField(default="",blank=True, null=True)
    imag4 = models.ImageField(default="",blank=True, null=True)
    imag5 = models.ImageField(default="",blank=True, null=True)
    imag6 = models.ImageField(default="",blank=True, null=True)
    imag7 = models.ImageField(default="",blank=True, null=True)
    imag8 = models.ImageField(default="",blank=True, null=True)
    dance_name = models.CharField(max_length=100,blank=True, default = "", null=True)
    food_name = models.CharField(max_length=100,blank=True, default = "", null=True)
    cheap_hotel = models.CharField(max_length=100,blank=True, default = "", null=True)
    mid_range_hotel = models.CharField(max_length=100,blank=True, default = "", null=True)
    five_star_hotel = models.CharField(max_length=100,blank=True, default = "", null=True)

    def __str__(self):
        return self.name
    
    
class BUS(models.Model):
    Bus_name = models.CharField(max_length=100, default = "")
    Bus_No = models.IntegerField()
    Source_Station_Name = models.CharField(max_length= 300)
    Destination_Station_Name = models.CharField(max_length= 300)
    days = models.CharField(max_length=50)
    sleeper = models.IntegerField(default=0,blank=True, null=True)
    AC = models.IntegerField(default=0,blank=True, null=True)
    
    def __str__(self):
        return self.Bus_name
    
class My_Flight(models.Model):
    Flight_name = models.CharField(max_length=100, default = "")
    Flight_No = models.IntegerField()
    Source_Station_Name = models.CharField(max_length= 300)
    Destination_Station_Name = models.CharField(max_length= 300)
    time = models.IntegerField()
    days = models.CharField(max_length=50)
    Economy = models.IntegerField(default=0,blank=True, null=True)
    Bussiness = models.IntegerField(default=0,blank=True, null=True)
    
    def __str__(self):
        return self.Flight_name
    
    
class Booking(models.Model):
    Train_No = models.IntegerField()
    Train_Name = models.CharField(max_length= 300)
    Source_Station_Name = models.CharField(max_length= 300)
    Destination_Station_Name = models.CharField(max_length= 300)
    contact_name = models.CharField(max_length=100, default = "")
    contact_number = models.CharField(max_length= 300)
    contact_gender = models.CharField(max_length=10, default="male")
    price = models.CharField(max_length= 300)
    age = models.CharField(max_length= 300)
    date = models.CharField(max_length=150)
    def __str__(self):
        return self.contact_name
    
class BusBooking(models.Model):
    Bus_No = models.IntegerField()
    Bus_Name = models.CharField(max_length= 300)
    Source_Station_Name = models.CharField(max_length= 300)
    Destination_Station_Name = models.CharField(max_length= 300)
    contact_name = models.CharField(max_length=100, default = "")
    contact_number = models.CharField(max_length= 300)
    contact_gender = models.CharField(max_length=10, default="male")
    price = models.CharField(max_length= 300)
    age = models.CharField(max_length= 300)
    date = models.CharField(max_length=150)
    def __str__(self):
        return self.contact_name
    
class FlightBooking(models.Model):
    Flight_No = models.IntegerField()
    Flight_Name = models.CharField(max_length= 300)
    Source_Station_Name = models.CharField(max_length= 300)
    Destination_Station_Name = models.CharField(max_length= 300)
    contact_name = models.CharField(max_length=100, default = "")
    contact_number = models.CharField(max_length= 300)
    contact_gender = models.CharField(max_length=10, default="male")
    price = models.CharField(max_length= 300)
    age = models.CharField(max_length= 300)
    date = models.CharField(max_length=150)
    def __str__(self):
        return self.contact_name
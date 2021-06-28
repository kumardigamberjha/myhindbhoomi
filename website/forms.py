from django.db.models import fields
from django.forms import ModelForm, models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import BusBooking, FlightBooking, Messages, Booking


class UserMessage(ModelForm):
    class Meta:
        model= Messages
        fields = ['email', 'message']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name","last_name", "username","email","password1", 'password2']

class UserBookings(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        
class Bus_Booking(ModelForm):
    class Meta:
        model = BusBooking
        fields = "__all__"
        
class Flight_Booking(ModelForm):
    class Meta:
        model = FlightBooking
        fields = "__all__"
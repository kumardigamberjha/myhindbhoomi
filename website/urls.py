from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("SignUp/", views.Signup_view, name="signup"),
    path('login/', views.Login_view, name="login"),
    path('logout/', views.Logout_view, name="logout"),
    path('rail/', views.rail, name="rail"),
    path('bus/', views.Bus, name="bus"),
    path('Flight/', views.Flight, name="flight"),
    path('Booking/<int:id>/', views.Bookings, name="booking"),
    path('Bus_Booking/<int:id>/', views.Bus_Bookings, name="bus_booking"),
    path('Flight_Booking/<int:id>/', views.Flight_Bookings, name="flight_booking"),
    path('Booked/', views.Booked, name="booked"),
    path('flightBooked/<int:id>/', views.render_flight_ticket, name="flightbooked"),
    path('flightBookedall/', views.myflight_TicketBooked, name="allflightbooked"),
    
    
    path('MyBookedTicket/<int:id>/', views.render_ticket, name="bookedticket"), 
    path('BusBookedTicket/<int:id>/', views.render_bus_ticket, name="renderbookedticket"),
    
    path('BusBookedTicket/', views.BusTicketBooked, name="busbookedticket"),
    path('YourBookings/', views.home_booking, name="yourbookings"),
    
    path('tour-guide/', views.TourGuide, name="tour-guide"),
    path('state-wise-tour-guide/<int:state_id>/', views.state_wise_tourism, name="state-wise-tourism"),
    
    
    # path('find_train/<train_id>,', views.find_train_btw_station, name="find_train")
]
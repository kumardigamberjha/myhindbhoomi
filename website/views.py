from io import BytesIO
from django.shortcuts import render, redirect
from django.template import context
from .models import FlightBooking, Train_Btw_Station, state, Messages,BUS, My_Flight, Booking, BusBooking
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserMessage, UserBookings, Bus_Booking, Flight_Booking
from django.contrib import messages



# index 
def index(request):
    todo= Messages(email= request.POST.get('email'), message=request.POST.get('msg'))
    todo.save()
    return render(request, 'website/index.html')

def Logout_view(request):
    logout(request)
    return redirect('login')


def Signup_view(request):
    form = CreateUserForm()
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    if request.method=='POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for "+ user+ " succesfully")
            return redirect('login')

    return render(request, 'website/signup.html', {'form':form})

def Login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

        else:
            messages.info(request, 'Invalid username/password')

    return render(request, 'website/login.html')

train_date = "" 

@login_required(login_url="/login/")
def rail(request):
    train = Train_Btw_Station.objects.all()
    Source_Station_Name = ""
    Destination_Station_Name = ""
    global train_date
    if request.method=="POST":
        Source_Station_Name = request.POST.get('source_station')
        Destination_Station_Name = request.POST.get('destination_station')
        train_date = request.POST.get('train_dates')

    src_query = Source_Station_Name
    print(src_query)
    print('train_date: ', train_date)
    dst_query = Destination_Station_Name
    context = {'train': train, 'src_query': src_query, 'dst_query': dst_query, 'train_date: ': train_date}

    return render(request, 'website/rail.html', context,)
    
def find_train_btw_station(request, train_id):
    return render(request, 'website/rail.html')

def TourGuide(request):
    states = state.objects.all()
    context = {'states': states}
    return render(request, 'website/guide.html', context)

def state_wise_tourism(request, state_id):
    states = state.objects.get(id = state_id)
    context = {'states': states}
    return render(request, 'website/state-wise-tour.html', context)

Bus_date = "" 
@login_required(login_url="/login/")
def Bus(request):
    bus_data = BUS.objects.all()
    Source_Station_Name = ""
    Destination_Station_Name = ""
    global Bus_date
    if request.method=="POST":
        Source_Station_Name = request.POST.get('source_station')
        Destination_Station_Name = request.POST.get('destination_station')
        Bus_date = request.POST.get('date')
    src_query = Source_Station_Name
    dst_query = Destination_Station_Name
    context = {'bus': bus_data, 'src_query': src_query, 'dst_query': dst_query}
    return render(request, 'website/bus.html', context)

Flight_date = ""
@login_required(login_url="/login/")
def Flight(request):
    flight = My_Flight.objects.all()
    Source_Station_Name = ""
    Destination_Station_Name = ""
    global Flight_date
    if request.method=="POST":
        Source_Station_Name = request.POST.get('source_station')
        Destination_Station_Name = request.POST.get('destination_station')
        Flight_date = request.POST.get('date')
    src_query = Source_Station_Name
    dst_query = Destination_Station_Name
    context = {'flight': flight, 'src_query': src_query, 'dst_query': dst_query}
    return render(request, 'website/Flight.html', context)

@login_required(login_url="/login/")
def Bookings(request, id):
    rail = Train_Btw_Station.objects.get(id = id)
    global train_date
    form = UserBookings()

    if request.method == "POST":
        Train_No = request.POST.get('Train_No')       
        Train_Name = request.POST.get("Train_Name")
        Source_Station_Name = request.POST.get("Source_Station_Name")
        Destination_Station_Name = request.POST.get('Destination_Station_Name')
        contact_name = request.POST.get('contact_name')
        age = request.POST.get('age')
        contact_number = request.POST.get('contact_number')
        contact_gender = request.POST.get('contact_gender')
        price = request.POST.get('price')
        date = train_date
        
        form = UserBookings(request.POST)
        if form.is_valid():
            form.save()

    print(Train_No)

    context = {'train':rail, 'form':form, 'date':date}
    return render(request, "website/Bookings.html",context)


@login_required(login_url="/login/")
def Bus_Bookings(request, id):
    bus_data = BUS.objects.get(id = id)
    global Bus_date
    
    form = Bus_Booking()

    if request.method == "POST":
        Bus_No = request.POST.get('Bus_No')       
        Bus_Name = request.POST.get("Bus_Name")
        Source_Station_Name = request.POST.get("Source_Station_Name")
        Destination_Station_Name = request.POST.get('Destination_Station_Name')
        contact_name = request.POST.get('contact_name')
        age = request.POST.get('age')
        contact_number = request.POST.get('contact_number')
        contact_gender = request.POST.get('contact_gender')
        price = request.POST.get('price')
        date = Bus_date
        print(Bus_Name)
        form = Bus_Booking(request.POST)
        if form.is_valid():
            form.save()

    print(date)

    context = {'bus_data':bus_data, 'form':form, 'date': date}
    return render(request, 'website/Bus_booking.html', context)

@login_required(login_url="/login/")
def Flight_Bookings(request, id):
    flight = My_Flight.objects.get(id = id)
    global Flight_date    
    form = Flight_Booking()
    if request.method == "POST":
        Flight_No = request.POST.get('Flight_No')       
        Flight_Name = request.POST.get("Flight_name")
        Source_Station_Name = request.POST.get("Source_Station_Name")
        Destination_Station_Name = request.POST.get('Destination_Station_Name')
        contact_name = request.POST.get('contact_name')
        age = request.POST.get('age')
        contact_number = request.POST.get('contact_number')
        contact_gender = request.POST.get('contact_gender')
        price = request.POST.get('price')
        date = Flight_date
        form = Flight_Booking(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()

    context = {'flight':flight, 'form':form, 'date': date}
    return render(request, 'website/flight_booking.html', context)

def Booked(request):
    books = Booking.objects.all()
    context = {'books': books}
    return render(request, 'website/Booked.html', context)

def render_ticket(request, id):
    books = Booking.objects.get(id = id)
    context = {'books': books}
    return render(request, 'website/render_ticket.html', context)

def BusTicketBooked(request):
    books = BusBooking.objects.all()
    context = {'books': books}
    return render(request, 'website/BusBooked.html', context)

def render_bus_ticket(request, id):
    books = BusBooking.objects.get(id = id)
    context = {'books': books}
    return render(request, 'website/render_bus_ticket.html', context)

def home_booking(request):
    return render(request, 'website/booking-home.html')

def myflight_TicketBooked(request):
    books = FlightBooking.objects.all()
    context = {'books': books}
    return render(request, 'website/allflightbooked.html', context)

def render_flight_ticket(request, id):
    books = FlightBooking.objects.get(id = id)
    context = {'books': books}
    return render(request, 'website/flightbooked.html', context)

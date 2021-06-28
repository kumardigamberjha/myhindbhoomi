from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import My_Flight, Train_Btw_Station, myTrains, state, Messages, BUS, Booking, BusBooking, FlightBooking



@admin.register(Train_Btw_Station)
class Train_info_Resources(ImportExportModelAdmin):

    class Meta:
        model = Train_Btw_Station
        

@admin.register(myTrains)
class Train_Schedule(ImportExportModelAdmin):

    class Meta:
        model = myTrains

admin.site.register(state)
admin.site.register(Messages)
admin.site.register(BUS)
admin.site.register(My_Flight)
admin.site.register(Booking)
admin.site.register(BusBooking)
admin.site.register(FlightBooking)


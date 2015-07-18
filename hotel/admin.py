from django.contrib import admin
from models import *

'''
class ModelBAdmin(admin.ModelAdmin):

    def modelA_Codes(self, inst):
        return ','.join([b.code for b in inst.modela_set.all()])

    list_display = ('name', 'modelA_Codes')
'''

class HotelAdmin(admin.ModelAdmin):

    list_display = ['name', 'rating', 'logo', 'rooms', 'hotel_id']


class HotelRoomsAdmin(admin.ModelAdmin):

    list_display = ['type_id', 'type_name', 'total', 'available', 'rate', 'beds']


admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelRooms, HotelRoomsAdmin)
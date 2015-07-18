from django.db import models

'''
hotel_hard_code = {
    'hotel_id': '24',
    'name' : 'Le Meriden',
    'rating' : '4.5',
    'logo' : 'someurl',
    'rooms': [
        {
            'type_id': 0,
            'type_name': 'Local',
            'total': 30,
            'available': 24,
            'rate': 399,
            'beds': 2

        },
        {
            'type_id': 1,
            'type_name': 'Delux',
            'total': 20,
            'available': 15,
            'rate': 799,
            'beds': 3

        }
    ]
}
'''


class HotelRooms(models.Model):
    related_hotel_id = models.CharField(max_length=20, null=True)
    type_id = models.CharField(max_length=20)
    type_name = models.CharField(max_length=200)
    total = models.CharField(max_length=20)
    available = models.CharField(max_length=20)
    rate = models.CharField(max_length=20)
    beds = models.CharField(max_length=20)


class Hotel(models.Model):
    hotel_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=10)
    logo = models.CharField(max_length=500)
    rooms = models.ForeignKey(HotelRooms, null=True)
    #rooms = HotelRooms


class Appliances(models.Model):
    hotel_id = models.CharField(max_length=20, null=True)
    room_number = models.CharField(max_length=20, null=True)
    appliance_id = models.CharField(max_length=20, null=True)
    on = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=20, null=True)


class Room(models.Model):
    hotel_id = models.CharField(max_length=200, null=True)
    user = models.CharField(max_length=200, default=0, null=True)
    room_server = models.CharField(max_length=200, null=True)
    room_number = models.CharField(max_length=20, null=True)
    type_id = models.CharField(max_length=20, null=True)
    type_name = models.CharField(max_length=20, null=True)
    appliances = models.ForeignKey(Appliances, null=True)
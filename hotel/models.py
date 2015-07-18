from django.db import models

'''
hotel_hard_code = {
    'name' : 'Le Meriden',
    'rating' : '4.5',
    'logo' : 'someurl',
    'rooms': [
        {
            'type_id': 0,
            'type_name': 'Local',
            'total': 30,
            'available': 40,
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

class Hotel(models.Model):
    hotel_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=10)
    logo = models.CharField(max_length=500)
    rooms = HotelRooms()


class HotelRooms(models.Model):
    type_id = models.CharField(max_length=20)
    type_name = models.CharField(max_length=200)
    total = models.CharField(max_length=20)
    available = models.CharField(max_length=20)
    rate = models.CharField(max_length=20)
    beds = models.CharField(max_length=20)
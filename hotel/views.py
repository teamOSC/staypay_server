from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, HttpResponse
import json
import requests
from hotel.models import HotelRooms, Hotel, Appliances, Room


# my functions know what you did in the app..

def mainPage(request):
    print "hello"
    return HttpResponse('shubham')


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


def hotelId(request, hotel_id):

    try:
        hotel_data = {}
        print hotel_id
        a = Hotel.objects.get(hotel_id=hotel_id)
        hotel_data['name'] = a.name
        hotel_data['hotel_id'] = a.hotel_id
        hotel_data['logo'] = a.logo
        hotel_data['rating'] = a.rating
        hotel_data['rooms'] = []
        b = HotelRooms.objects.filter(related_hotel_id=hotel_id)
        for x in b:
            filler_dict = {}
            av = Room.objects.filter(hotel_id=hotel_id, type_id=str(x.type_id), user='0')
            filler_dict['type_id'] = str(x.type_id)
            filler_dict['type_name'] = str(x.type_name)
            filler_dict['total'] = str(x.total)
            #filler_dict['available'] = str(x.available)
            filler_dict['available'] = av
            x.available = av
            filler_dict['rate'] = str(x.rate)
            filler_dict['beds'] = str(x.beds)
            x.save()
            hotel_data['rooms'].append(filler_dict)

        #print hotel_data
        return HttpResponse(json.dumps(hotel_data), content_type='application/json')
    except:
        pass

    return HttpResponse(json.dumps(hotel_hard_code), content_type='application/json')


def bookRoom(request, hotel_id, room_type):

    print "USER"

    user_id = request.GET.get('user_id')
    cmd = request.GET.get('cmd')

    try:
        a = Room.objects.get(hotel_id=hotel_id, type_id=room_type, user='0')
        print a, "============"
        a.user = user_id
        print a.room_number

        b = HotelRooms.objects.get(related_hotel_id=hotel_id, type_id=room_type)
        b.available = str(int(b.available) - 1)


        json_res = {
            'success': 'true',
            'room_no': a.room_number
        }

        a.save()
        b.save()

        return HttpResponse(json.dumps(json_res), content_type='application/json')

    except:
        pass

    return HttpResponse('some_error')


def unlock_gate(request, hotel_id, room_number, room_type):
    return HttpResponse(json.dumps({'success': 'true'}), content_type='application/json')
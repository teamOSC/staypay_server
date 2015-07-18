from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, HttpResponse
import json
import requests


# my functions know what you did in the app..

def mainPage(request):
    print "hello"
    return HttpResponse('shubham')


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


@csrf_exempt
def hotelId(request, hotel_id):

    try:
        user_id = request.POST.get('user_id')
    except:
        user_id = 'send me a POST request'

    json_value = {
        'status': hotel_id,
        'POST-data': {
            'user-id': user_id,
        },
        'summary': 'It just works if you see this.'
    }

    return HttpResponse(json.dumps(hotel_hard_code), content_type='application/json')
from django.http import HttpResponse, JsonResponse, FileResponse

from thirdparty import juhe

import json

def helloworld(request):
    print('request method:', request.method)
    print('request MATE:', request.META)
    print('request cookies:', request.COOKIES)
    print('request queryDict:', request.GET)
    # result = HttpResponse(content='hello django response',status=500 )

    m = {
        'message':'hello django response'
    }
    result = JsonResponse(data=m, safe=False, status=201)
    return result

def query_weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data = juhe.weather(city)
    elif request.method == 'POST':
        received_body = request.body
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        response_data = []
        for city in cities:
            result = juhe.weather(city)
            result['city']=city
            response_data.append(result)
        return JsonResponse(data=response_data, safe=False, status=200)

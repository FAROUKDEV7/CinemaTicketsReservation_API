from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest , Movie , Reservation

#1 First Way (without rest and no model query) 
def no_rest_no_model(request):
    guests = [
        {
            "id" : 1,
            "name" : "Ahmed",
            "mobile" : 12346,

        },
        {
            "id" : 2,
            "name" : "Mohamed",
            "mobile" : 52121,

        },
        {
            "id" : 3,
            "name" : "Kareem",
            "mobile" : 55112,

        },
    ]
    return JsonResponse(guests , safe=False)


#2 Model Data Default Django No Rest
def no_rest_from_model(request):
    guest =  Guest.objects.all()
    response = {
        'guests' : list(guest.values('name' , 'mobile'))
    }
    return JsonResponse(response)
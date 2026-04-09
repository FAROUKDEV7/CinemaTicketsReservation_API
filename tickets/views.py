from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import Http404
from rest_framework import status , mixins , generics , viewsets
from rest_framework.views import APIView
from .models import Guest , Movie , Reservation
from rest_framework.decorators import api_view
from .serializers import GuestSerializer , MovieSerializer , ReservationSerializer
from rest_framework.response import Response


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


#3 Function Based View
#3.1 GET POST
@api_view(['GET' , 'POST'])
def FBV_List(request):

    # GET
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests , many = True)
        return Response(serializer.data)
    
    # POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)
    
#3.2 GET PUT DELETE
@api_view(['GET' , 'PUT' , 'DELETE'])
def FBV_pk(request , pk):
    
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    # GET
    if request.method == 'GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    # PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        return Response(serializer.data , status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        guest.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#4 Class Based Views
#4.1 GET POST
class CBV_List(APIView):

    # GET
    def get(self , request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests , many=True)
        return Response(serializer.data)
    # POST
    def post(self , request):
        serializer = GuestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST)
    

# 4.2 GET PUT DELETE
class CBV_PK(APIView):

    # query set
    def get_object(self , pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
        

    # GET
    def get(self , request , pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    # PUT
    def put(self , request , pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest ,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

    # Delete
    def delete(self , request ,pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


    

# 5 mixins
# 5.1 GET POST
class mixins_list(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self , request):
        return self.list(request)
    
    def post(self , request):
        return self.create(request)
    

# 5.2 GET PUT DELETE
class mixins_pk(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin , generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

    def get(self , request , pk):
        return self.retrieve(request)
    
    def put(self , request , pk):
        return self.update(request)
    
    def delete(self , request , pk):
        return self.destroy(request)
    


# 6 generics
# 6.1 GET POST
class generic_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

# 6.2 GET PUT DELETE
class generic_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


# 7 viewsets
class viewsets_guests(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
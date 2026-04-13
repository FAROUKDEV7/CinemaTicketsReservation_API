from django.contrib import admin
from django.urls import path , include
from tickets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guests' , views.viewsets_guests)
router.register('movies' , views.viewsets_movie)
router.register('reservations' , views.viewsets_reservation)


urlpatterns = [
    path('admin/', admin.site.urls),

    # 1
    path("django/jsonresponsenomodel" , views.no_rest_no_model),

    # 2
    path("django/jsonresponsefrommodel" , views.no_rest_from_model),


    # 3.1 GET POST From Rest Framework Function Based View @api_view
    path("rest/FBV_List" , views.FBV_List),

    # 3.2 GET PUT DELETE From Rest Framework Function Based View @api_view
    path("rest/FBV_List/<int:pk>" , views.FBV_pk),


    # 4.1 GET POST From Rest Framework Class Based View APIView
    path("rest/CBV_List" , views.CBV_List.as_view()),


    # 4.2 GET PUT DELETE From Rest Framework Class Based View APIView
    path("rest/CBV_List/<int:pk>" , views.CBV_PK.as_view()),
    

    # 5.1 GET POST From Rest Framework Class Based View Mixins
    path("rest/mixins_list" , views.mixins_list.as_view()),


    # 5.2 GET PUT DELETE From Rest Framework Class Based View generics
    path("rest/mixins_list/<int:pk>" , views.mixins_pk.as_view()),

    # 6.1 GET POST From Rest Framework Class Based View Mixins
    path("rest/generic_list" , views.generic_list.as_view()),


    # 6.2 GET PUT DELETE From Rest Framework Class Based View generics
    path("rest/generic_list/<int:pk>" , views.generic_pk.as_view()),


    # 7 viewsets
    path("rest/viewsets",include(router.urls)),

    # find movie
    path("fvb/findmovie" , views.findmovie),

    # new reservation
    path("fvb/newreservation" , views.newreservation),

    # rest api auth
    path("api-auth/", include("rest_framework.urls")),
]

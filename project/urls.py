from django.contrib import admin
from django.urls import path , include
from tickets import views

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
    


]

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




]

from django.urls import path
from payments import views


urlpatterns = [

    path('create-discharge/',views.create_discharge,name='create-discharge'),
    path('bill/<int:pk>/',views.discharge_bill,name='discharge_bill'),
    path('bill-list/',views.discharge_list,name='discharge_list'),

]
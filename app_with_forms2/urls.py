from django.urls import path

from .views import customer_form,customers_list
urlpatterns=[
    path('',customer_form,name='costumer_form'),
    path('list/',customers_list,name='customers_list')
]
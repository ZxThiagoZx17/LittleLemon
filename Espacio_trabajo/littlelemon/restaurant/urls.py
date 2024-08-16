from django.contrib import admin 
from django.urls import path, include
from .views import ItemViewSet_reservas, ItemViewSet
from rest_framework import routers
  
router = routers.DefaultRouter()
router.register(r'ELementos_a_modificar', ItemViewSet)

urlpatterns = [ 
    # path('', sayHello, name='sayHello'), 
    path('', include(router.urls)), 
]
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Menus, Reservas
from .serializers import ItemSerializer

# Create your views here.
# def sayHello(request):
#     return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Menus.objects.all()
    serializer_class = ItemSerializer

class ItemViewSet_reservas(viewsets.ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ItemSerializer
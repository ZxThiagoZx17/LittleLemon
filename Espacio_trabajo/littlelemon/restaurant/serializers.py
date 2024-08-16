from rest_framework import serializers
from .models import Menus, Reservas

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ["Price", "id", "Title"]

class ItemSerializer_reservas(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'

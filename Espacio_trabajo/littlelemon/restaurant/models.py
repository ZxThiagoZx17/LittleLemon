from django.db import models

# Create your models here.
class Reservas(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return f"Reserva {self.id} para {self.nombre}"
    
class Menus(models.Model):
    id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits= 10, decimal_places=2)
    Inventory = models.IntegerField()

    def __str__(self):
        return self.Title
    

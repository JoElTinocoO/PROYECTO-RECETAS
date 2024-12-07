from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre de la receta
    categoria = models.CharField(max_length=100)  # Categoría (Ej. Postre, Entrada)
    fecha_creacion = models.DateField(auto_now_add=True)  # Fecha de creación automática
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")  # Tiempo de preparación en minutos
    ingredientes = models.TextField()  # Ingredientes necesarios
    instrucciones = models.TextField()  # Instrucciones para preparar

    def __str__(self):
        return self.nombre

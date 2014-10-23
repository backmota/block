from django.db import models


# Create your models here.
class juego(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    portada = models.ImageField(upload_to='static')
    precio = models.CharField(max_length=500)


    def __unicode__(self):
        return self.nombre
from datetime import date
from django.db import models
from django.conf import settings
from django.urls import reverse
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices
from trix.fields import TrixField


class Declaracion(models.Model):
    ESTADOS = Choices('borrador', 'publicado')
    fecha_publicacion = MonitorField(monitor='estado', when=['publicado'], editable=False)
    cargado_por = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    título = models.CharField(max_length=100)
    fecha = models.DateField(default=date.today())
    declaración = TrixField()
    

    estado = StatusField(choices_name='ESTADOS')
    nota_interna = models.TextField(blank=True, null=True)

    #PLANTILLA = Choices('actual','nueva')
    #apunta a la clase de mis nuevos template
    plantilla = models.ForeignKey('Plantilla', null=True)
    
    

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('estado', '-fecha', '-id')

class Plantilla(models.Model):
    # unique: que no deje repetir el nombre  
    nombre = models.CharField(max_length=100,unique=True)
    # deja subir archivos desde el admin
    archivo= models.FileField(upload_to='', max_length=200)

    #devuelve el string de un objeto
    def __str__(self):
        return self.nombre
    



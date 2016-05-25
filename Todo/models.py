from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __unicode__(self):
        return '{0}'.format(self.nombre)


class Tarea(models.Model):

    titulo = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'

    def __unicode__(self):
        return self.titulo

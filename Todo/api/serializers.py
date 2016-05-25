from rest_framework import serializers
from Todo.models import Categoria, Tarea


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')


class TareaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarea
        fields = ('id', 'titulo', 'categoria', 'descripcion')

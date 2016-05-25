from rest_framework import serializers
from Todo.models import Categoria, Tarea


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')


class TareaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(many=True, source='categoria')
    class Meta:
        model = Tarea
        fields = ('id', 'titulo', 'categoria__nombre', 'descripcion')

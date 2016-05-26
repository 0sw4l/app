from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from serializers import TareaSerializer, CategoriaSerializer
from Todo.models import Categoria, Tarea


@api_view(['GET', 'POST'])
def categoria_list(request):
    """
        crear y listar categorias
    """
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail(request, pk):
    try:
        categoria = Categoria.objects.get(id=pk)
    except Categoria.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def tarea_list(request):

    if request.method == 'GET':
        tareas = Tarea.objects.all().order_by('-id')
        serializer = TareaSerializer(tareas, many=True)
        return Response({'items': serializer.data})

    elif request.method == 'POST':
        serializer = TareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def tarea_detail(request, pk):
    """
    item
    """
    try:
        tarea = Tarea.objects.get(id=pk)
    except Tarea.DoesNotExist:
        return Response(status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = TareaSerializer(tarea)
        return Response({'items': serializer.data})
    elif request.method == 'PUT':
        serializer = TareaSerializer(tarea, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tarea.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework import viewsets
from .models import Cliente, Pedido
from .serializers import ClienteSerializer, PedidoSerializer

# ViewSet encargado de gestionar las operaciones CRUD de clientes
class ClienteViewSet(viewsets.ModelViewSet): # Especifica el conjunto de datos (queryset) que se va a utilizar,
    # en este caso obtiene todos los registros del modelo Cliente
    queryset = Cliente.objects.all()
    # Indica qué serializer se usará para convertir los datos del modelo Cliente
    # a formato JSON y viceversa (entrada y salida de datos en la API)
    serializer_class = ClienteSerializer

# ViewSet encargado de gestionar las operaciones CRUD de pedidos
class PedidoViewSet(viewsets.ModelViewSet):
    # Obtiene todos los pedidos almacenados en la base de datos
    queryset = Pedido.objects.all()
    # Serializer encargado de transformar los datos de Pedido a JSON
    serializer_class = PedidoSerializer

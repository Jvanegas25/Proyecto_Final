from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("""
    <h1>API Gestión de Pedidos</h1>
    <p>API para gestionar clientes y pedidos.</p>

    <h2>Endpoints</h2>

    <h3>Clientes</h3>
    <ul>
        <li>GET /api/clientes/</li>
        <li>POST /api/clientes/</li>
        <li>GET /api/clientes/{id}/</li>
        <li>PUT /api/clientes/{id}/</li>
        <li>DELETE /api/clientes/{id}/</li>
    </ul>

    <h3>Pedidos</h3>
    <ul>
        <li>GET /api/pedidos/</li>
        <li>POST /api/pedidos/</li>
        <li>GET /api/pedidos/{id}/</li>
        <li>PUT /api/pedidos/{id}/</li>
        <li>DELETE /api/pedidos/{id}/</li>
    </ul>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('', index),
]

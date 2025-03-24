"""
URL configuration for SmartNutri project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from usuario.api.router import usuario_router
from cliente.api.router import cliente_router
from receita.api.router import receita_router
from nutricionista.api.router import nutricionista_router
from ingrediente.api.router import ingrediente_router
from acompanhamento.api.router import acompanhamento_router
from planoalimentar.api.router import planoalimentar_router
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuario/', include(usuario_router.urls)),
    path('api/cliente/', include(cliente_router.urls)),
    path('api/receita/', include(receita_router.urls)),
    path('api/nutricionista/', include(nutricionista_router.urls)),
    path('api/ingrediente/', include(ingrediente_router.urls)),
    path('api/acompanhamento/', include(acompanhamento_router.urls)),
    path('api/planoalimentar/', include(planoalimentar_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
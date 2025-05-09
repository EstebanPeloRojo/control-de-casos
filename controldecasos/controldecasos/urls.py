"""optica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from . import settings
from django.conf.urls.static import static
from casos import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('usuarios.urls')),
    path('casos/', include('casos.urls')),
    path('api-auth/', include('rest_framework.urls')),
    #path('', include('casos.urls')),
    
    # path('formulario', views.formulario, name='formulario') esta linea no va aca 
    #url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    #url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATICFILES_DIRS}),
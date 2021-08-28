
import pessoa
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pessoa.urls')),
    path('admin/', admin.site.urls),
]

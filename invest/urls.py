from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('invest/stocks/', include('stocks.urls')),
    path('admin/', admin.site.urls),
]
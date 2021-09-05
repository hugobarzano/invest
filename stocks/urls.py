from django.urls import path

from . import views

app_name = 'stocks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:stock_name>/', views.detail, name='detail'),
    path('<str:stock_name>/data_api', views.detail_as_json, name='detail_as_json'),
    path('<str:stock_name>/data', views.detail_as_json, name='detail_from_elastic_json'),

]

from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import JsonResponse
from .models import *

from .client.client import *

class IndexView(generic.ListView):
    template_name = 'stocks/index.html'
    context_object_name = 'stocks_list'

    def get_queryset(self):
        """Return the last five"""
        return Stock.objects.order_by('-created')[:5]


def detail(request, stock_name):
    stock = get_object_or_404(Stock, name=stock_name)
    return render(request, 'stocks/detail.html', {'stock': stock})

def detail_as_json(request,stock_name):
    date = []
    open = []

    c = Client("EGS9M9PKVRPCC946")
    status, body = c.get_stock_data(stock_name)

    time_serie_key = "Time Series (5min)"
    for k in body[time_serie_key]:
        date.append(k)
        open.append(body[time_serie_key][k]["1. open"])
    return JsonResponse(data={
        'date': date,
        'open': open,
    })
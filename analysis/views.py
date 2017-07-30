from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import StockName, StockPrices
from django.core.urlresolvers import reverse
from django.views.generic import View,ListView
from .forms import *
import datetime
from django import template

class StockListView(View): 
    def get(self, request, *args, **kwargs ):             
        object_list = StockName.objects.all()
        return render( request,"stocks/stocklist.html", { 'object_list':object_list  } )
        

class StockPriceListView(View):
     
    def get(self, request, *args, **kwargs ):
        stockId = int( request.GET.get( "id", 0 ) )
        stockName=StockName.objects.get(pk=stockId)
        object_list = StockPrices.objects.filter(stock_id=stockId)
        percentageChange=[]
        for stock in object_list:
            percentageChange.append(stock.stock_close-stock.stock_open)
            
        object_volumelist=object_list.order_by('-stock_volume')[:5]       
        return render( request,"stocks/stockpricelist.html", { 'object_list':object_list ,'percentage_change':percentageChange,'stockName':stockName,'volumelist':object_volumelist } )

class StockListDelete(View):     
    def get(self, request, *args, **kwargs ):
        stockId = request.GET.get('id', '')
        StockName.objects.get(pk=stockId).delete() 
        return HttpResponseRedirect('analysis/stock/list/')
    

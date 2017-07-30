from django.conf.urls import url
from . import views
urlpatterns = [
 
         url(r'^$',views.StockListView.as_view(), name='stock_list'),
         url(r'^stockprices/list/$',views.StockPriceListView.as_view(), name='stockprices_list'),
         url(r'^stock/delete/$',views.StockListDelete.as_view(), name='stock_delete'),          
]


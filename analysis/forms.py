
from django import forms
from django.forms import ModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import StockName, StockPrices
from django.core.urlresolvers import reverse
from django.views.generic import View,ListView

class StockDetailsForm( forms.Form ):
    class Meta:
        model = StockPrices
        # stock_id = forms.ChoiceField(
        #            label = "Item",
        #            choices = [('', '---Select---')],
        #            widget = forms.Select( attrs = { 'class': 'selectpicker'} ),                  
        #            required = False)

        stock_date = forms.CharField(
                   label = "Stock Date",
                   max_length = 100,
                   widget = forms.TextInput(
                                attrs = {
                                            "placeholder": "eg: 6asd7asd#@",
                                            "class": "form-control",
                                            "autocomplete": "off"
                                }
                   ),
                   required = True)

        stock_open = forms.CharField(
                       label = "Open",
                       widget = forms.TextInput(
                                     attrs = {
                                                "placeholder": "eg:1,2,3..",
                                                 "class": "form-control numeric",
                                                 "autocomplete": "off"
                                    }
                       ),
                       required = True)
        
        stock_high = forms.CharField(
                       label = "High",
                       widget = forms.TextInput(
                                     attrs = {
                                                "placeholder": "eg:1,2,3..",
                                                 "class": "form-control numeric",
                                                 "autocomplete": "off"
                                    }
                       ),
                       required = True)
        
        stock_low = forms.CharField(
                       label = "Low",
                       widget = forms.TextInput(
                                     attrs = {
                                                "placeholder": "eg:1,2,3..",
                                                 "class": "form-control numeric",
                                                 "autocomplete": "off"
                                    }
                       ),
                       required = True)
        
        
        stock_close = forms.CharField(
                       label = "Close",
                       widget = forms.TextInput(
                                     attrs = {
                                                "placeholder": "eg:1,2,3..",
                                                 "class": "form-control numeric",
                                                 "autocomplete": "off"
                                    }
                       ),
                       required = True)
        
        
        
        
        stock_volume = forms.CharField(
                       label = "Volume",
                       widget = forms.TextInput(
                                     attrs = {
                                                "placeholder": "eg:1,2,3..",
                                                 "class": "form-control numeric",
                                                 "autocomplete": "off"
                                    }
                       ),
                       required = True)

    def __init__(self, *args, **kwargs):
        super(StockDetailsForm,self).__init__(*args, **kwargs)     
        # self.fields['stock_id'].empty_label = "---Select---"
        # stock_id_choices = StockName.objects.values_list('id', 'name')
        # stock_id_choices = [x for x in stock_id_choices]
        # self.fields['stock_id'].choices = stock_id_choices
        
   

import uuid, os
from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext as _

class StockQueryForm(forms.Form):
    stockCode = forms.CharField(required=True,\
        label = _("stock.code"),\
        widget = forms.TextInput(attrs={'class':'text'})\
        )   

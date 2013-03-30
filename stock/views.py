# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from stock.forms import StockQueryForm

def showQueryForm(request):
    form = StockQueryForm()
    html = "stock/query_form.html" 
    parameters = {"form":form}
    return __return(html, parameters, request)

def query(request):
    form = StockQueryForm(request.POST)
    html = "stock/stock.html"
    parameters = {"stock_code":"600835"}
    return __return(html, parameters, request)

def getProfile(request):
    html = "stock/stock_profile.html"
    parameters = {}
    return __return(html, parameters, request)

def getFinanceIndex(request):
    html = "stock/finance_index.html"
    parameters = {}
    return __return(html, parameters, request)

def getFinancePrediction(request):
    html = "stock/finance_prediction.html"
    parameters = {}
    return __return(html, parameters, request)

def getFinanceIndexRank(request):
    html = "stock/finance_index_rank.html"
    parameters = {}
    return __return(html, parameters, request)

def __return(html, parameters, request):
    return render_to_response(html,parameters, RequestContext(request))

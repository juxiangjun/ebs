from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^showQueryForm', 'stock.views.showQueryForm'),
    url(r'^query', 'stock.views.query'),
    url(r'^getProfile', 'stock.views.getProfile'),
    url(r'^getFinanceIndex', 'stock.views.getFinanceIndex'),
    url(r'^getFinancePrediction', 'stock.views.getFinancePrediction'),
    url(r'^getFinanceIndexRank', 'stock.views.getFinanceIndexRank'),
)

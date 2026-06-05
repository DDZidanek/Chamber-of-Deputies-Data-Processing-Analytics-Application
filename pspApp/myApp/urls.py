from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.baseView, name='index'),
    path("tables/",views.tableView, name="tables"),
    path("charts/",views.chartView, name="charts"),
    path("clustering/",views.clusteringView, name="cluster"),
    path("test/",views.testView, name="test"),
]

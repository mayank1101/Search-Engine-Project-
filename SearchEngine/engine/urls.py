from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'search_results.html/$',views.search_results,name='search_results'),
    url(r'^$', views.index, name='index'),
]

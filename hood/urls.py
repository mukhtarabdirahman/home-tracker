from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^image_form/$', views.image_form, name='image_form'),
    url(r'^search/', views.search_results, name='search_results')
]
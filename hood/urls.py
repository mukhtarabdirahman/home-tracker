from django.conf.urls import url
from . import views

urlpatterns=[
    url('^home/$',views.home,name = 'home'),
    url(r'^image_form/$', views.image_form, name='image_form'),
]
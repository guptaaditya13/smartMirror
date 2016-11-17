from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^enqueue/$', views.enqueue, name = 'enqueue'),
	url(r'^dequeue/$', views.dequeue, name = 'dequeue'),
]
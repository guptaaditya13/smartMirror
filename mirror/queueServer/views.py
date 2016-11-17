from django.shortcuts import render
from django.http import HttpResponse
from queueServer.models import *
from django.core.serializers.json import DjangoJSONEncoder
import json

# Create your views here.
def enqueue(request):
	if request.method == 'POST':
		inp = request.body.decode('utf-8')
		json_data = json.loads(inp)
		#consider json_data as an associative array
		#add to the queue here
		obj = QueueEntry(data = inp)
		obj.save()
		return HttpResponse(200)

def dequeue(request):
	obj_list = QueueEntry.objects.all()
	json_list = []
	for obj in obj_list:
		json_list.append(obj.data)
	return HttpResponse(json.dumps(json_list, cls=DjangoJSONEncoder))
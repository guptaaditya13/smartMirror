from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from queueServer.models import *
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
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
	count = QueueEntry.objects.count()
	if count > 0 :
		obj_list = QueueEntry.objects.all()[:1]
		print (obj_list)
		for obj in obj_list:
			obj.delete()
			return HttpResponse(obj.data)
	else:
		print('sending 400 response code')
		return HttpResponseNotFound('Sorry')
	

def viewMirror(request):
	return render(request, 'home.html')
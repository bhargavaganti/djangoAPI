from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from zipcodeendpoint.serializers import ZipAdjacencySerializer
from zipcodeendpoint.models import ZipAdjacency
# Create your views here.
def index(requests):
	return HttpResponse("Hello, world. you are on the index page")

@csrf_exempt
def zipcode_list(request):
	if request.method == 'GET':
		zipcodes = ZipAdjacency.objects.all()
		serializer = ZipAdjacencySerializer(zipcodes, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ZipAdjacencySerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def zipcode_detail(request, pk):
	try:
		zipcode = ZipAdjacency.objects.get(pk=pk)
	except ZipAdjacency.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ZipAdjacencySerializer(zipcode, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)
	elif request.method == 'DELETE':
		zipcode.delete()
		return HttpResponse(status=204)

#class ZipList(generics.ListCreateAPIView):
#	queryset = ZipAdjacency.objects.all()
#	serializer_class = ZipAdjacencySerializer

#class ZipDetail(generics.RetrieveUpdateDestroyAPIView):
#	queryset = ZipAdjacency.objects.all()
#	serializer_class = ZipAdjacencySerializer
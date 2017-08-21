from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import Http404

from zipcodeendpoint.serializers import ZipAdjacencySerializer
from zipcodeendpoint.models import ZipAdjacency
from rest_framework import mixins 
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions


# Create your views here.
def index(requests):
	return HttpResponse("Hello, world. you are on the index page")

class ZipcodeList(mixins.ListModelMixin,
	mixins.CreateModelMixin,
	generics.GenericAPIView):
	lookup_field = 'zip_code'
	lookup_url_kwarg = 'zip_code'
	#queryset = ZipAdjacency.objects.all() #.filter(zip_code= "{}".format(args.zip_code))
	serializer_class = ZipAdjacencySerializer

	def get_queryset(self):
		zip_code= self.kwargs.get(self.lookup_url_kwarg)
		queryset = ZipAdjacency.objects.filter(zip_code=zip_code)
		return queryset

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class ZipcodeDetail(mixins.RetrieveModelMixin,
	mixins.UpdateModelMixin,
	mixins.DestroyModelMixin,
	generics.GenericAPIView):
	queryset = ZipAdjacency.objects.all()
	serializer_class = ZipAdjacencySerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(slef, request, *args, **kwargs):
		return slef.destroy(request, *args, **kwargs)



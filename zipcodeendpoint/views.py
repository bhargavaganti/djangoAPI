from django.http import HttpResponse 
# Create your views here.
def index(requests):
	return HttpResponse("Hello, world. you are on the index page")
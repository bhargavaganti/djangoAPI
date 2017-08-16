from django.conf.ulrs import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]
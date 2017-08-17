from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from zipcodeendpoint import views
from . import views


# TODO ziplist? what is this
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^zipcodeendpoint/$', views.zipcode_list),
	url(r'^zipcodeendpoint/(?P<pk>[0-9 ]+)/$', views.zipcode_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
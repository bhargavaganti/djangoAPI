from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from zipcodeendpoint import views
from . import views


# TODO ziplist? what is this
urlpatterns = [
	###url(r'^$', views.index, name='index'),
	url(r'^zipcode/$', views.ZipcodeList.as_view()),
	url(r'^zipcode/(?P<zip_code>[0-9]+)/$', views.ZipcodeList.as_view()),
	url(r'^zipcode/(?P<pk>[0-9]+)/$', views.ZipcodeDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
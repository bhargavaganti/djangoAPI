from rest_framework import serializers
from zipcodeendpoint.models import ZipAdjacency

class ZipAdjacencySerializer(serializers.ModelSerializer):
	class Meta:
		model = ZipAdjacency
		fields = ('zip_code', 'adj_zip')
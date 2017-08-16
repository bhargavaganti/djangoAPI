from django.db import models

# Create your models here.
class ZipAdjacency(models.Model):
    zip_code = models.TextField(blank=True, null=True)
    adj_zip = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'zip_adjacency'

class CountyAdjacency(models.Model):
    county = models.TextField(blank=True, null=True)
    county_geoid = models.TextField(blank=True, null=True)
    adj_county = models.TextField(blank=True, null=True)
    adj_county_geoid = models.TextField(blank=True, null=True)
	class Meta:
        managed = False
        db_table = 'county_adjacency'
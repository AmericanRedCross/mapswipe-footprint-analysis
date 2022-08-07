from django.db import models
from django.contrib.gis.db import models as geom 


# Create your models here.


class Building(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    idx = models.FloatField(blank=True, null=True)
    task_id = models.CharField(max_length=255, blank=True, null=True)
    number_0_count = models.FloatField(db_column='0_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_count = models.FloatField(db_column='1_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_count = models.FloatField(db_column='2_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_count = models.FloatField(db_column='3_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    total_count = models.FloatField(blank=True, null=True)
    number_0_share = models.FloatField(db_column='0_share', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_share = models.FloatField(db_column='1_share', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2_share = models.FloatField(db_column='2_share', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_3_share = models.FloatField(db_column='3_share', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    agreement = models.FloatField(blank=True, null=True)
    unnamed_0 = models.FloatField(db_column='unnamed: 0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    changesetid = models.FloatField(blank=True, null=True)
    lastedit = models.DateTimeField(blank=True, null=True)
    osmid = models.CharField(max_length=255, blank=True, null=True)
    version = models.FloatField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    editor = models.CharField(max_length=255, blank=True, null=True)
    userid = models.FloatField(blank=True, null=True)
    wkb_geometry = geom.MultiPolygonField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'building'


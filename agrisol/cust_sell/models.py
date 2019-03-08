from django.db import models

# Create your models here.
class seller(models.Model):
    name = models.CharField(max_length=25)
    rate = models.IntegerField()
    images = models.FileField(null=True, blank=True, upload_to="static/seller/images")
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=25)

    state = (('Punjab', 'Punjab'),
           ('Delhi', 'Delhi'),
           ('Bihar', 'Bihar'),
           ('UP', 'UP'),
             ('Orissa', 'Orissa'),
           ('Haryana', 'Haryana'),
           ('Meghalaya', 'Meghalaya'),

           )


class customer(models.Model):
    name = models.CharField(max_length=25)
    #place = models.IntegerField(max_length=25)
    mobile_number = models.CharField(max_length=10)




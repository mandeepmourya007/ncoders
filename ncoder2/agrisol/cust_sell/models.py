from django.db import models

# Create your models here.
class seller(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25,default="")
    rate = models.IntegerField()
    images = models.FileField(null=True, blank=True, upload_to="static/seller/images")
    state = (('Punjab', 'Punjab'),
             ('Delhi', 'Delhi'),
             ('Bihar', 'Bihar'),
             ('UP', 'UP'),
             ('Orissa', 'Orissa'),
             ('Haryana', 'Haryana'),
             ('Meghalaya', 'Meghalaya'),

             )

    state = models.CharField(max_length=25,choices=state,default='Punjab')
    city = models.CharField(max_length=25)
    def __str__(self):
        return self.first_name



class customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25,default="")
    #place = models.IntegerField(max_length=25)
    mobile_number = models.CharField(max_length=10)
    def __str__(self):
        return self.first_name

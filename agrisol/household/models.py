from django.db import models

# Create your models here.
class flowers(models.Model):
    name = models.CharField(max_length=25)
    images = models.FileField(null=True, blank=True, upload_to="static/crops/images")
    description = models.TextField(max_length=200)
    seasonf = (('Spring', 'Spring'),
             ('Summer', 'Summer'),
             ('Autumn', 'Autumn'),
             ('Winter', 'Winter'),

             )

    season = models.CharField(max_length=40, choices=seasonf,
        default='Summer')
    success_ratio = models.CharField(max_length=3)

    def __str__(self):
        return self.name

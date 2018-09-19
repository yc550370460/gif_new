from django.db import models

# Create your models here.


class Image(models.Model):
    STATUS = (("OK", "OK"),
              ("notOK", "notOK"),
              ("ongoing", "ongoing"))

    status = models.CharField(max_length=7, choices=STATUS)
    active = models.BooleanField()
    path = models.ImageField(upload_to="gif/static/img/")
    name = models.CharField(max_length=100)
    weight = models.IntegerField(default=1)
    date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return self.name
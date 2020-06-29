from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=45)
    tech = models.CharField(max_length=15)
    describ = models.CharField(max_length=100)
    link = models.CharField(max_length=100,default=None,null=True,blank=True)
    def __str__(self):
        return self.title
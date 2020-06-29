from django.db import models

# Create your models here.
class works(models.Model):
    title = models.CharField(max_length=20)
    discrib = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics',max_length=50,default='asd')
    links = models.CharField(max_length=30,default=None,null=True)
    def __str__(self):
        return self.title
    

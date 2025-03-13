from django.db import models

class Book(models.Model):
    title = models.CharField("სათაური" , max_length = 18 , null=False, blank = False)
    author = models.CharField("ავტორი" , max_length = 18 , null=False, blank = False)
    published_date = models.DateField()
    published_date = models.DateField()
    genres = models.ManyToManyField(Genre)

class genres(models.Model):
    name = models.CharField("ჟანრი", max_length=50, null=False, blank=False)
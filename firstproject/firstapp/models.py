from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length = 250, unique = True)

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    page_name = models.CharField(max_length = 250, unique = True)
    url = models.URLField(unique = True)

class Record(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

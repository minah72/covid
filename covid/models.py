from django.db import models

class Covid(models.Model):
    Date = models.CharField(max_length=100, blank=True)
    Country = models.CharField(max_length=100, blank=True)
    Confirmed = models.CharField(max_length=1000000, blank=True)
    Recovered = models.CharField(max_length=1000000, blank=True)
    Deaths = models.CharField(max_length=1000000, blank=True)

    def __str__(self):
        return self.name
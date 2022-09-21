from logging.handlers import WatchedFileHandler
from django.db import models

class BarangMywatchlist (models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length = 255)
    rating = models.IntegerField()
    release_date = models.DateField()
    review = models.CharField(max_length = 255)
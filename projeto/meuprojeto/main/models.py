from django.db import models
from datetime import datetime as dt

class ProjetoFilmes(models.Model):
    titulo = models.CharField(max_length=30)
    filme1 = models.CharField(max_length=30)
    filme2 = models.CharField(max_length=30)
    filme3 = models.CharField(max_length=30)
    filme4 = models.CharField(max_length=30)
    filme5 = models.CharField(max_length=30)
    data = models.DateTimeField("Lista publicada em", default=dt.now())

    def __str__(self):
        return self.titulo

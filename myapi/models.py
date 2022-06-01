from django.db import models

# Create your models here.

class prenatal(models.Model):
    name = models.CharField(max_length=60)
    mae = models.CharField(max_length=60)
    cns = models.CharField(max_length=60)
    unidade = models.CharField(max_length=60)

    def __str__(self):
        return self.name


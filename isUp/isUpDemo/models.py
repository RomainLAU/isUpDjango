from django.db import models


class Domain(models.Model):
    domain = models.CharField(max_length=253)
    is_up = models.BooleanField(null=True, blank=True)
    # owner = models.ForeignKey()


class Check:
    status = models.BooleanField()
    last_check = models.DateTimeField()

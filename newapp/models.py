from django.db import models

# New device model
class Devices(models.Model):
    name = models.CharField(max_length=30)
    os = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    secret = models.CharField(max_length=30)
    port = models.IntegerField()
    def __str__(self):
        return self.name
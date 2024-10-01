from django.db import models

# Create your models here.
class study(models.Model):
    name = models.CharField(max_length=122)
    phase = models.CharField(max_length=122)
    sponsorName = models.CharField(max_length=122)
    description = models.TextField()

    def __str__(self):
        return self.name

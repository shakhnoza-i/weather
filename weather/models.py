from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=255)
    current_temperature = models.IntegerField()
    desc = models.CharField(max_length=225)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.city
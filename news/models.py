from django.db import models

# Create your models here.

class MavzuNomi(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name

class HomeModels(models.Model):
    name = models.CharField(max_length=210)
    body = models.TextField()
    mavzu = models.ForeignKey(MavzuNomi, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

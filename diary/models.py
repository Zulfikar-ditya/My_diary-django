from django.db import models
from django.contrib.auth.models import User

class MyDiary(models.Model):
    date_add = models.DateField(auto_now=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    value = models.CharField(max_length=10000)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def delete(self, **kwargs):
        self.status = False
        self.save()
        


from django.db import models

# Create your models here.
class storage(models.Model):
    key=models.IntegerField(primary_key=True,auto_created=True)
    url=models.CharField(max_length=100)
    list_words=models.CharField(max_length=100)

    def __str__(self):
        return str(self.key)
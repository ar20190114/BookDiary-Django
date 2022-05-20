from django.db import models

# Create your models here.
class SelfBookModel(models.Model):
    selfbooktitle = models.CharField(max_length=100)

    selfbookname = models.CharField(max_length=100)

    selfbookimage = models.ImageField(upload_to='media')

    selfbookcomment = models.TextField()

    selfbookendday = models.DateField()

    def __str__(self):
        return self.selfbooktitle
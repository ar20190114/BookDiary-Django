from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=100)

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='media')

    comment = models.TextField()

    endday = models.DateField()

    def __str__(self):
        return self.title
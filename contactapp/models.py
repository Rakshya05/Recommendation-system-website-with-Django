from django.db import models

# Create your models here.
class contacts(models.Model):
    # Define your model fields here
    email = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.email
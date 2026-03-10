from django.db import models

class EidCard(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='cards/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

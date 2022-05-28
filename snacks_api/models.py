from django.db import models
from django.contrib.auth import get_user_model

class Snack(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

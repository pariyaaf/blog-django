from django.db import models
from common.models import BaseModel

class BloggerModel(BaseModel):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name

from django.db import models
from common.models import BaseModel

class BloggerModel(BaseModel):

    __name__ = "bloggers"

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/bloggers/%Y/%m")
    birth_date = models.DateField(blank=True)
    #register date
    post_count = models.IntegerField(default=0)
    bio = models.TextField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name

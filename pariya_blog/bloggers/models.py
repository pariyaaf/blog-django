from django.db import models
from common.models import BaseModel
from django.contrib.auth.models import User
class BloggerModel(BaseModel):

    __name__ = "bloggers"

    # user
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, default=0)

    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/bloggers/%Y/%m")
    birth_date = models.DateField(blank=True, null=True)
    #register date
    post_count = models.IntegerField(default=0)
    bio = models.TextField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=16)

    def __str__(self):
        return self.name

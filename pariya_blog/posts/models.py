from django.db import models
from common.models import BaseModel
from bloggers.models import BloggerModel
from datetime import datetime


class PostModel(BaseModel):

    __tablename__ = "posts"

    blogger = models.ForeignKey(BloggerModel, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    comments_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    # post_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/', blank=True)

    def __str__(self) -> str:
        return self.title



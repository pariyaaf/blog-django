from django.db import models
from datetime import datetime
from posts.models import PostModel
from common.models import BaseModel


class CommentModel(BaseModel):
    user_email = models.CharField(max_length=255)
    user_name = models.CharField(max_length=200)
    comment_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField()
    is_published = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.comment_text
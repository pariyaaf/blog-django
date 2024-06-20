from django.db import models
from datetime import datetime

class CommentModel(models.Model):
    user_email = models.CharField(max_length=255)
    user_name = models.CharField(max_length=200)
    commet_date = models.DateTimeField(auto_now_add=True)
    post_id = models.IntegerField()
    comment_text = models.TextField()

    def __str__(self) -> str:
        return self.comment_text
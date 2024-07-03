from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']  # فیلدهایی که در فرم استفاده می‌شوند باید با مدل مطابقت داشته باشند
        labels = {
            'comment_text': 'متن کامنت',
        }
        widgets = {
            'post': forms.HiddenInput(),
        }
from django import forms
from .models import CommentModel

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['user_email', 'comment_text', 'user_name', 'post']  # فیلدهایی که در فرم استفاده می‌شوند باید با مدل مطابقت داشته باشند
        labels = {
            'user_email': 'ایمیل',
            'comment_text': 'متن کامنت',
            'user_name': 'نام کاربری',
        }
        widgets = {
            'post': forms.HiddenInput(),
        }
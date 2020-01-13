from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'content',)

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'content': forms.Textarea(attrs={'placeholder': 'Отзыв'}),
        }
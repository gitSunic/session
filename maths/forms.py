from django import forms
from .models import Ticket, MathImg


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

        widgets = {
            'num': forms.NumberInput(attrs={'placeholder': 'Номер билета'}),
            'name': forms.TextInput(attrs={'placeholder': 'Название билета'}),
        }


class MathImgForm(forms.ModelForm):
    class Meta:
        model = MathImg
        fields = '__all__'

        widgets = {
            'ticket': forms.HiddenInput()
        }

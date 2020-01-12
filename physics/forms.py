from django import forms
from .models import Ticket, PhysImg


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

        widgets = {
            'num': forms.NumberInput(attrs={'placeholder': 'Номер билета'}),
            'name': forms.TextInput(attrs={'placeholder': 'Название билета'}),
        }


class PhysImgForm(forms.ModelForm):
    class Meta:
        model = PhysImg
        fields = '__all__'

        widgets = {
            'ticket': forms.HiddenInput()
        }

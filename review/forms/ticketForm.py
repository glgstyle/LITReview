
from django import forms
from review.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
            model = Ticket
            fields = ['title', 'description', 'image']
            widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'autocomplete': 'OFF',
                'required': 'required'
                }),
            'description': forms.Textarea(attrs={
                'class': "form-control", 
                'id': 'book-description',
                'autocomplete': 'OFF'
                }),
            'image': forms.FileInput(attrs={
                    'class': 'btn btn-primary',
                    'type': 'file',
                    'id': 'button-uppload',
                    'value': 'Télécharger le fichier',
                    'label':'Télécharger le fichier'
                })
            }
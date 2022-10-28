
from cProfile import label
from django import forms
from review.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
            model = Ticket
            fields = ['title', 'author', 'description', 'image']
            label = {'image' : 'Télécharger'}
            widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'autocomplete': 'OFF',
                'required': 'required'
                }),
            'author': forms.TextInput(attrs={
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
                    # 'class': 'btn btn-primary',
                    'type': 'file',
                    'id': 'button-upload',
                    'style':'color:transparent;',
                    'name': 'button-uppload',
                    'label':'Télécharger le fichier',
                    'placeholder':'Télécharger le fichier',

                })
            }
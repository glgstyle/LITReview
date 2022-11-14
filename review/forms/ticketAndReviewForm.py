from review.models import Review
from review.models import Ticket
from django import forms
from django.forms.models import modelformset_factory


class TicketAndReviewForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'author', 'description', 'image']
        label = {'image': 'Télécharger'}
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
                'type': 'file',
                'id': "image-input",
                'style': 'color:transparent;',
                'name': 'button-uppload',
                'label': 'Télécharger le fichier',
                'placeholder': 'Télécharger le fichier',
            })
        }


ReviewFormset = modelformset_factory(
    Review,
    fields=['rating', 'headline', 'body'],
    widgets={
        'rating': forms.NumberInput(attrs={
            'class': "form-control",
            'id': "result",
            'autocomplete': 'OFF',
            'required': 'required'
        }),
        'headline': forms.TextInput(attrs={
            'class': "form-control",
            'id': "review-title",
            'autocomplete': 'OFF',
            'required': 'required',
        }),
        'body': forms.Textarea(attrs={
            'class': "form-control",
            'id': 'book-description',
            'autocomplete': 'OFF'
        })
    }
)

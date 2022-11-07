

from django import forms
from authentication.models import UserFollows


class SubscriptionForm(forms.ModelForm):
    class Meta:
            model = UserFollows
            fields = ['followed_user']
            widgets = {
            'followed_user': forms.TextInput(attrs={
                'class': "form-control",
                'id': 'first-input',
                'placeholder': "Nom d'utilisateur",
                'aria-label': "Recipient's username",
                'aria-describedby': 'button-addon2'
                })
            }

            # 'author': forms.TextInput(attrs={
            #     'class': "form-control",
            #     'autocomplete': 'OFF',
            #     'required': 'required'
            #     }),
            # 'description': forms.Textarea(attrs={
            #     'class': "form-control", 
            #     'id': 'book-description',
            #     'autocomplete': 'OFF'
            #     }),
            # 'image': forms.FileInput(attrs={
            #         # 'class': 'btn btn-primary',
            #         'type': 'file',
            #         'id': 'button-upload',
            #         'style':'color:transparent;',
            #         'name': 'button-uppload',
            #         'label':'Télécharger le fichier',
            #         'placeholder':'Télécharger le fichier',

                # })
            # }
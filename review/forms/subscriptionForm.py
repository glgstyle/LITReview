

from django import forms
# from authentication.models import UserFollows


class SubscriptionForm(forms.Form):
    class Meta:
            # model = UserFollows
            # base_fields = ['followed_user']
            followed_user = forms.CharField(label='Utilisateur', max_length=100, widget=forms.TextInput(attrs={'class': "form-control",
                'id': 'first-input',
                'placeholder': "Nom d'utilisateur",
                'aria-label': "Recipient's username",
                'aria-describedby': 'button-addon2'}))
            # widgets = {
            # 'followed_user': forms.TextInput(attrs={
            #     'class': "form-control",
            #     'id': 'first-input',
            #     'placeholder': "Nom d'utilisateur",
            #     'aria-label': "Recipient's username",
            #     'aria-describedby': 'button-addon2'
            #     })
            # }
            
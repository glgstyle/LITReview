from django import forms


class SubscriptionForm(forms.Form):
    followed_user = forms.CharField(label=False, max_length=100, widget=forms.TextInput(attrs={'class': "form-control",'id': 'first-input','placeholder': "Nom d'utilisateur",'aria-label': "Recipient's username",'aria-describedby': 'button-addon2'}))
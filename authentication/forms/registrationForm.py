from django import forms

class NewUserForm(forms.Form):
    your_email = forms.EmailField(label=False, max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre email'}))
    your_password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Votre mot de passe'}))
    confirmed_password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmation mot de passe'}))
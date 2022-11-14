from django import forms


class loginForm(forms.Form):
    username = forms.EmailField(label=False, max_length=100, widget=forms.
                                EmailInput(attrs={'class': 'form-control',
                                                  'placeholder': 'Username',
                                                  'autocomplete': 'OFF',
                                                  'required': 'required'}))
    password = forms.CharField(label=False, widget=forms.
                               PasswordInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Password',
                                                    'autocomplete':
                                                    'current-password',
                                                    'required': 'required'}))

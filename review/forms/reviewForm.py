from dataclasses import fields
from django import forms
from review.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
            model = Review
            fields = ['rating', 'headline', 'body']
            widgets = {
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
            
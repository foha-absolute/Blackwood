from django import forms
from shop.models import *


class ReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'review..'
    }))

    class Meta:
        model = ProductReview
        fields = ('review',)


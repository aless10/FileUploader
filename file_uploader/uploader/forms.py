from django import forms
from django.core.exceptions import ValidationError

from .utils import is_the_past


class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}
    ))
    password = forms.CharField(max_length=16, required=False, empty_value=None)
    expiry_date = forms.DateTimeField(required=False)

    def clean_expiry_date(self):
        expiry_date = self.cleaned_data.get('expiry_date')
        if expiry_date is not None and is_the_past(expiry_date):
            raise ValidationError("You can't set an already expired date")
        return expiry_date


class UnlockForm(forms.Form):
    password = forms.CharField(max_length=16)

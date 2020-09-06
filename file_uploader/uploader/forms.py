from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}
    ))
    password = forms.CharField(max_length=16, required=False, empty_value=None)
    expiry_date = forms.DateTimeField(required=False)

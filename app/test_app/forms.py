from django import forms
from .models import Person


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=15, required=False)
    files = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    file = forms.FileField(required=True)


class TestModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

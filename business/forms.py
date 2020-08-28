from django import forms
from .models import BusinessProfile
from tinymce.widgets import TinyMCE

article = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


class bp_model_form(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        fields = '__all__'

from django import forms
from .models import BusinessProfile
from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import Tab, TabHolder

article = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

about = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


class bp_model_form(forms.ModelForm):
    about = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = BusinessProfile
        exclude = ('user',)

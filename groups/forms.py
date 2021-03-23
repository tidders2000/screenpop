from django import forms
from .models import Groups
from tinymce.widgets import TinyMCE

about = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


class add_groups_form(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('groupName', 'groupLocation', 'about')

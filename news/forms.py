from django import forms
from .models import News
from tinymce.widgets import TinyMCE

article = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


class add_news_form(forms.ModelForm):
    class Meta:
        model = News
        fields = ('headline', 'image', 'article')

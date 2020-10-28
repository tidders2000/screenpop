from django import forms
from .models import Meeting, Apologies, Guests
from tinymce.widgets import TinyMCE


class DateInput(forms.DateInput):
    input_type = 'date'


class meeting_model_form(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'

        widgets = {
            'meeting_date': DateInput(),
        }


class apologies_form(forms.ModelForm):
    class Meta:
        model = Apologies
        fields = '__all__'


class guests_form(forms.ModelForm):
    class Meta:
        model = Guests
        fields = '__all__'


class status_form(forms.ModelForm):
    class Meta:
        model = Guests
        labels = {
            'status': '',
        }
        fields = ('status',)

from django import forms
from .models import BusinessProfile
from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import Tab, TabHolder

article = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))


class bp_model_form(forms.ModelForm):

    class Meta:
        model = BusinessProfile
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(
                Tab('Contact Details',
                    'contact_name',
                    'street_address1',
                    'street_address2',
                    'town_or_city',
                    'county',
                    'postcode',
                    'country',
                    'e_mail',
                    'phone',

                    ),
                Tab('Business Details',
                    'business_type',
                    'opening_hours',
                    'number_emp',
                    'location',
                    'legal_entity'

                    ),
                Tab('Social Media',
                    'facebook',
                    'twitter',
                    'linkedin',
                    'google',
                    'website'
                    ),
                Tab('Images',
                    'logo',
                    'header_image'

                    ),
                Tab('Services and About',
                    HTML(
                        '<a href="{% url "edit_profile_b" tpk %}">Click here to edit</a>')


                    )
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-danger')
            )
        )
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'


class tiny_model_form(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        fields = ('about', 'services')

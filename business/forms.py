from django import forms
from .models import BusinessProfile
from tinymce.widgets import TinyMCE
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import Tab, TabHolder

about = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 80}))


class bp_model_form(forms.ModelForm):

    class Meta:
        model = BusinessProfile
        fields = ('contact_name',
                  'street_address1',
                  'street_address2',
                  'town_or_city',
                  'county',
                  'postcode',
                  'country',
                  'e_mail',
                  'phone',
                  'facebook',
                  'twitter',
                  'linkedin',
                  'google',
                  'website',
                  'business_type',
                  'opening_hours',
                  'number_emp',
                  'location',
                  'legal_entity',
                  'logo',
                  'header_image')

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
                Submit('submit', 'Save', css_class='btn btn-danger')
            )
        )
        self.helper.form_id = 'id-exampleForm'
        self.helper.enc_type = "multipart/form-data"
        self.helper.form_method = 'POST'


class tiny_model_form(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        fields = ('about', 'services')

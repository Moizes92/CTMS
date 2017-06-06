from __future__ import absolute_import

from django import forms
from gpsdevices.models import GPSDevice
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions


class GPSDeviceForm(forms.ModelForm):
    name = forms.CharField(label='Device Name', widget=forms.TextInput())
    type = forms.CharField(label='Device Type', widget=forms.TextInput())
    imei = forms.CharField(label='Device IMEI', widget=forms.TextInput())
    sim_num = forms.CharField(label='SIM Card Number', widget=forms.TextInput())
    purchase_date = forms.DateField(label='Purchase_Date', widget=forms.DateInput(attrs={'type': 'date'}))
    assigned_to = forms.CharField(label='Assign To', widget=forms.TextInput())
    status = forms.ChoiceField(label='Status', choices=(('Installed', 'Installed'), ('Not Installed', 'Not Installed')))

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal col col-md-12'
    helper.form_method = 'POST'
    helper.field_class = 'col col-md-8'
    helper.label_class = 'col col-md-4'

    helper.layout = Layout(

        Div(
            Div(
                Field('name', css_class='form-control'),
                Field('type', css_class='form-control'),
                Field('imei', css_class='form-control'),
                Field('sim_num', css_class='form-control'),
                Field('purchase_date', css_class='form-control'),
                Field('assigned_to', css_class='form-control'),
                Field('status', css_class='form-control'), css_class='col col-md-6',
            ),
            Div(
                HTML('<br/>'),
                FormActions(
                    Submit('save', 'Save', css_class='btn btn-primary'),
                    Submit('cancel', 'Cancel', css_class='btn btn-danger'),
                ), css_class='col col-md-6 col-offset-2',
            ), css_class='row',
        ),
    )

    class Meta:
        model = GPSDevice
        fields = '__all__'

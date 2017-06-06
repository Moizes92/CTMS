from __future__ import absolute_import

from django import forms
from vehicle.models import Vehicle

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import FormActions, AppendedText, PrependedText


class VehicleForm(forms.ModelForm):

    licence_num = forms.CharField(label='Licence Number', widget=forms.TextInput())
    type = forms.CharField(label='Type', widget=forms.TextInput())
    engine_num = forms.CharField(label='Engine Number', widget=forms.TextInput())
    registration_date = forms.DateField(label='Date of Registration', widget=forms.DateInput(attrs={'type': 'date'}))
    number_of_seats = forms.IntegerField(label='Number of Seats', widget=forms.TextInput())
    color = forms.CharField(label='Body Color', widget=forms.TextInput())
    make = forms.CharField(label='Make', widget=forms.TextInput())
    model = forms.CharField(label='Model', widget=forms.TextInput())
    year = forms.CharField(label='Production Year', widget=forms.TextInput())
    body_type = forms.CharField(label='Body Type', widget=forms.TextInput())
    gas_type = forms.CharField(label='Gas Type', widget=forms.TextInput())
    date_of_purchase = forms.DateField(label='Purchase Date', widget=forms.DateInput(attrs={'type': 'date'}))
    km_read_at_purchase = forms.IntegerField(label='Millage at Purchase', widget=forms.TextInput())
    licence_renewal_date = forms.DateField(label='Licence Renewal Date', widget=forms.DateInput(attrs={'type': 'date'}))
    insurance_renewal_date = forms.DateField(label='Insurance Renewal Date', widget=forms.DateInput(attrs={'type': 'date'}))

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal col col-md-12'
    helper.form_method = 'POST'
    helper.field_class = 'col col-md-8'
    helper.label_class = 'col col-md-4'

    helper.layout = Layout(

        Div(
            Div(
                Field('licence_num', css_class='form-control'),
                Field('type', css_class='form-control'),
                Field('engine_num', css_class='form-control'),
                Field('registration_date', css_class='form-control'),
                Field('number_of_seats', css_class='form-control'),
                Field('color', rows="2", css_class='form-control'),
                Field('make', css_class='form-control'), css_class='col col-md-6',
            ),

            Div(
                Field('model', css_class='form-control'),
                Field('year', css_class='form-control'),
                Field('body_type', css_class='form-control', ),
                Field('gas_type', css_class='form-control'),
                Field('date_of_purchase', css_class='form-control'),
                Field('km_read_at_purchase', css_class='form-control', type='upload'),
                Field('licence_renewal_date', css_class='form-control', type='upload'),
                Field('insurance_renewal_date', css_class='form-control', type='upload'), css_class='col col-md-6',
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
        model = Vehicle
        fields = '__all__'

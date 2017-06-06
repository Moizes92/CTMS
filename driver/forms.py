from __future__ import absolute_import

from django import forms
from driver.models import Driver
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Field
from crispy_forms.bootstrap import FormActions


class DriverForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput())
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput())
    date_of_birth = forms.CharField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput())
    phone = forms.IntegerField(label='Phone Number', widget=forms.TextInput())
    address = forms.CharField(label='Address', widget=forms.Textarea())
    licence_category = forms.ChoiceField(label='Licence Category', choices=(('A', 'A'), ('A1', 'A1'), ('A2', 'A2'),
                                                                            ('A3', 'A3'), ('B', 'B'), ('C', 'C'),
                                                                            ('C1', 'C1'), ('C2', 'C2'), ('C3', 'C3'),
                                                                            ('D', 'D'), ('E', 'E'), ('F', 'F'),
                                                                            ('G', 'G')))
    licence_id = forms.CharField(label='Licence ID', widget=forms.TextInput())
    issuing_authority = forms.ChoiceField(label='Issuing Authority', choices=(('TRA', 'TRA'), ('ZRA', 'ZRA'),
                                                                              ('International', 'International')))
    licence_issue_date = forms.DateField(label='Licence Issue Date', widget=forms.DateInput(attrs={'type': 'date'}))
    licence_expiry_date = forms.DateField(label='Licence Expiry Date', widget=forms.DateInput(attrs={'type': 'date'}))
    status = forms.ChoiceField(label='Status', choices=(('Inactive', 'Inactive'), ('Active', 'Active')))
    profile_pic = forms.ImageField(label='Profile Picture', )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal col col-md-12'
    helper.form_method = 'POST'
    helper.field_class = 'col col-md-8'
    helper.label_class = 'col col-md-4'

    helper.layout = Layout(

        Div(
            Div(
                Field('first_name', css_class='form-control'),
                Field('last_name', css_class='form-control'),
                Field('date_of_birth', css_class='form-control'),
                Field('email', css_class='form-control'),
                Field('phone', css_class='form-control'),
                Field('address', rows="2", css_class='form-control'),
                Field('licence_category', css_class='form-control'), css_class='col col-md-6',
            ),

            Div(
                Field('licence_id', css_class='form-control'),
                Field('issuing_authority', css_class='form-control'),
                Field('licence_issue_date', css_class='form-control', ),
                Field('licence_expiry_date', css_class='form-control'),
                Field('status', css_class='form-control'),
                Field('profile_pic', css_class='form-control', type='upload'), css_class='col col-md-6',
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
        model = Driver
        fields = '__all__'

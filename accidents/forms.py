from __future__ import absolute_import

from django import forms
from driver.models import Driver
from vehicle.models import Vehicle
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Field, Row
from crispy_forms.bootstrap import FormActions


class AccidentForm(forms.ModelForm):
    ACCIDENT_CAUSES = (
        ("", "----------"),
        ("Overspeeding", "Overspeeding"),
        ("Distracted Driving", "Distracted Driving"),
        ("Driver Fatigue", "Driver Fatigue"),
        ("Drunk Driving", "Drunk Driving"),
        ("Rubber-necking", "Rubber-necking"),
        ("Defective Automobile", "Defective Automobile"),
        ("Roadway Construction Defects", "Roadway Construction Defects"),
        ("Poor Weather Conditions", "Poor Weather Conditions"),
        ("Animal Crossings", "Animal Crossings"),
        ("Tire Blowouts", "Tire Blowouts"),
        ("Potholes", "Potholes"),
        ("Other", "Other")
    )
    vehicle = forms.ModelChoiceField(label='Vehicle', queryset=Vehicle.objects.all())
    driver = forms.ModelChoiceField(label='Driver Responsible', queryset=Driver.objects.all())
    date_of_accident = forms.CharField(label='Date Accident Occurred', widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.CharField(label='Location', widget=forms.TextInput())
    cause = forms.ChoiceField(label='Possible Cause', choices=ACCIDENT_CAUSES)
    description = forms.CharField(label='Brief Description', widget=forms.Textarea())
    image = forms.ImageField(label='Accident Image', )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal col col-md-12'
    helper.form_method = 'POST'
    helper.field_class = 'col col-md-8'
    helper.label_class = 'col col-md-4'

    helper.layout = Layout(

        Div(
            Div(
                Field('vehicle', css_class='form-control'),
                Field('driver', css_class='form-control'),
                Field('date_of_accident', css_class='form-control'),
                Field('location', css_class='form-control'),
                css_class='col col-md-6',
            ),
            Div(
                Field('cause', css_class='form-control'),
                Field('description', rows="4", css_class='form-control'),
                Field('image', css_class='form-control', type='upload'), css_class='col col-md-6',
            ),
        ),
        Div(
            Div(
                HTML('<br/>'),
                FormActions(
                    Submit('save', 'Save', css_class='btn btn-primary btn-sm'),
                    Submit('cancel', 'Cancel', css_class='btn btn-danger btn-sm'),
                ), css_class='col col-md-6 col-offset-2',
            )
        )
    )


    class Meta:
        model = Driver
        fields = '__all__'

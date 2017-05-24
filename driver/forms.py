from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form

from vehicle.models import Vehicle


class DriverForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    license_category = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    license_renewal_date = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    image = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )

    class Meta:
        model = Vehicle
        fields = [
            'plate_num',
            'model',
            'brand',
            'color',
            'production_year',
            'date_of_purchase',
            'km_read_at_purchase',
            'license_renewal_date',
            'insurance_renewal_date',
            'current_driver',
            'status',
        ]


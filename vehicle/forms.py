from django import forms
from django.core.exceptions import ValidationError
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm, Form

from vehicle.models import Vehicle


class VehicleForm(forms.ModelForm):

    plate_num = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    model = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    maker = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    color = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    production_year = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    date_of_purchase = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    km_read_at_purchase = forms.IntegerField(
        widget=forms.IntegerInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    license_renewal_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    insurance_renewal_date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    current_driver = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True
    )
    status = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
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


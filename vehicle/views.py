from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Avg, Sum
from vehicle.models import Vehicle
from braces.views import LoginRequiredMixin
import datetime


class VehicleListView(ListView):

    model = Vehicle
    fields = ['nickname', 'license_id', 'current_driver', 'vehicle_model', 'maker']
    template_name = 'vehicle/vehicles_list.html'


class CreateVehicleView(CreateView):

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
    template_name = 'vehicle/add_vehicle.html'

    def get_success_url(self):
        return reverse('vehicles_list')

    def get_context_data(self, **kwargs):
        context = super(CreateVehicleView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_vehicle')

        return context


class UpdateVehicleView(UpdateView):

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
    template_name = 'vehicle/edit_vehicle.html'

    def get_success_url(self):
        return reverse('vehicles_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateVehicleView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_vehicle', kwargs={'pk': self.get_object().id})
        return context


class DeleteVehicleView(DeleteView):

    model = Vehicle
    success_url = reverse_lazy('vehicles_list')


class VehicleView(DetailView):

    model = Vehicle
    template_name = 'vehicle/vehicle.html'


def view_vehicle(request, pk):

    today = datetime.datetime.today()
    next_week = datetime.date.today()+datetime.timedelta(days=7)
    next_month = datetime.date.today()+datetime.timedelta(days=31)

    # next license renewals:
    vehicle = Vehicle.objects.get(id=pk)

    if vehicle.license_renewal_date < next_week:
        license_renewal = 1
    elif vehicle.license_renewal_date < next_month:
        license_renewal = 2
    else:
        license_renewal = 3

    # next insurance renewals:
    if vehicle.insurance_renewal_date < next_week:
        insurance_renewal = 1
    elif vehicle.insurance_renewal_date < next_month:
        insurance_renewal = 2
    else:
        insurance_renewal = 3

    """try:
        km = KMRead.objects.filter(license_id=car.id).\
            latest('timestamp').value
    except:
        km = "No km Data!"
    accidents_cost = Accident.objects.\
        filter(license_id_id=pk).\
        aggregate(value_sum=Sum('cost'))
    try:
        monthly_record = MonthlyRecord.objects.filter(license_id=car.id).\
            latest('id')
    except:
        monthly_record = "No Data!"
    try:
        treatment = Treatment.objects.filter(license_id=car.id).\
            latest('id')
        if (km - treatment.km_read < 1000):
            km1000 = True
        else:
            km1000 = False
    except:
        treatment = "No Data!"
        km1000 = False """
    try:
        next_vehicle = Vehicle.objects.get(pk=pk+1)
    except:
        next_vehicle = None
    try:
        previous_vehicle = Vehicle.objects.get(pk=pk-1)
    except:
        previous_vehicle = None
    context = dict(
        vehicle=vehicle,
        today=today,
        license_renewal=license_renewal,
        insurance_renewal=insurance_renewal,
        # km=km,
        # km1000=km1000,
        # monthly_record=monthly_record,
        # treatment=treatment,
        # accidents_cost=accidents_cost['value_sum'],
        next_vehicle=next_vehicle,
        previous_vehicle=previous_vehicle,
    )
    return render(request, 'vehicle/view_vehicle.html', context)



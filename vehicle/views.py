from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from vehicle.models import Vehicle
from driver.models import Driver
from django.utils.translation import ugettext_lazy as _
from vehicle.forms import VehicleForm
from braces.views import LoginRequiredMixin, FormMessagesMixin


class VehicleListView(ListView):

    model = Vehicle
    template_name = 'vehicle/vehicles_list.html'


class CreateVehicleView(FormMessagesMixin, CreateView):

    extra_context = {'object_name': _(u'Vehicle')}
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle/add_vehicle.html'
    form_valid_message = 'Vehicle was successfully created!'
    form_invalid_message = 'There are some errors found in form. Please check the data and resubmit.'

    def get_success_url(self):
        return reverse('vehicles_list')

    def get_context_data(self, **kwargs):
        context = super(CreateVehicleView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_vehicle')
        return context


class UpdateVehicleView(FormMessagesMixin, UpdateView):

    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle/edit_vehicle.html'
    form_valid_message = 'Vehicle was successfully updated!'
    form_invalid_message = 'There are some errors found in form. Please check the data and resubmit.'

    def get_success_url(self):
        return reverse('vehicles_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateVehicleView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_vehicle', kwargs={'pk': self.get_object().id})
        return context


class DeleteVehicleView(FormMessagesMixin, DeleteView):

    model = Driver
    template_name = 'vehicle/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicles_list')
    form_valid_message = 'Vehicle was deleted successfully!'


class VehicleView(DetailView):

    model = Vehicle
    template_name = 'vehicle/view_vehicle.html'

    # def view_vehicle(request, pk):
    #
    #     today = datetime.datetime.today()
    #     next_week = datetime.date.today()+datetime.timedelta(days=7)
    #     next_month = datetime.date.today()+datetime.timedelta(days=31)
    #
    #     # next licence renewals:
    #     vehicle = Vehicle.objects.get(id=pk)
    #
    #     if vehicle.licence_renewal_date < next_week:
    #         licence_renewal = 1
    #     elif vehicle.licence_renewal_date < next_month:
    #         licence_renewal = 2
    #     else:
    #         licence_renewal = 3
    #
    #     # next insurance renewals:
    #     if vehicle.insurance_renewal_date < next_week:
    #         insurance_renewal = 1
    #     elif vehicle.insurance_renewal_date < next_month:
    #         insurance_renewal = 2
    #     else:
    #         insurance_renewal = 3
    #     try:
    #         km = KMRead.objects.filter(licence_id=car.id).\
    #             latest('timestamp').value
    #     except:
    #         km = "No km Data!"
    #     accidents_cost = Accident.objects.\
    #         filter(licence_id_id=pk).\
    #         aggregate(value_sum=Sum('cost'))
    #     try:
    #         monthly_record = MonthlyRecord.objects.filter(licence_id=car.id).\
    #             latest('id')
    #     except:
    #         monthly_record = "No Data!"
    #     try:
    #         treatment = Treatment.objects.filter(licence_id=car.id).\
    #             latest('id')
    #         if (km - treatment.km_read < 1000):
    #             km1000 = True
    #         else:
    #             km1000 = False
    #     except:
    #         treatment = "No Data!"
    #         km1000 = False
    #     try:
    #     next_vehicle = Vehicle.objects.get(pk=pk+1)
    #
    # except:
    #     next_vehicle = None
    # try:
    #     previous_vehicle = Vehicle.objects.get(pk=pk-1)
    # except:
    #     previous_vehicle = None
    # context = dict(
    #     vehicle=vehicle,
    #     today=today,
    #     licence_renewal=licence_renewal,
    #     insurance_renewal=insurance_renewal,
    #     km=km,
    #     km1000=km1000,
    #     monthly_record=monthly_record,
    #     treatment=treatment,
    #     accidents_cost=accidents_cost['value_sum'],
    #     next_vehicle=next_vehicle,
    #     previous_vehicle=previous_vehicle,
    # )
    # return render(request, 'vehicle/view_vehicle.html', context)

# class MonthlyListView(ListView):
#
#     model = MonthlyRecord
#     template_name = 'monthly/records_list.html'
#
#
# class CreateMonthlyView(FormMessagesMixin, CreateView):
#
#     model = MonthlyRecord
#     fields = ['vehicle', 'year', 'month', 'fuel_consumed', 'cost', 'km']
#     template_name = 'monthly/add_monthly.html'
#     form_valid_message = 'Vehicle was successfully created!'
#     form_invalid_message = 'There are some errors found in form. Please check the data and resubmit.'
#
#     def get_success_url(self):
#         return reverse('records_list')
#
#     def get_context_data(self, **kwargs):
#         context = super(CreateMonthlyView, self).get_context_data(**kwargs)
#         context['target'] = reverse('add_record')
#
#         return context
#
#
# class CreateMonthlyViewVehicle(FormMessagesMixin, CreateView):
#
#     model = MonthlyRecord
#     fields = ['vehicle', 'year', 'month', 'fuel_consumed', 'cost', 'km']
#     template_name = 'monthly/add_monthly.html'
#
#     def get_success_url(self):
#         return reverse('records_list')
#
#     def get_context_data(self, **kwargs):
#         context = super(CreateMonthlyView, self).get_context_data(**kwargs)
#         context['target'] = reverse('add_record',
#                                     kwargs={'pk': Vehicle.objects.get(id=self.kwargs['pk'])})
#
#         return context
#
#
# class UpdateMonthlyView(FormMessagesMixin, UpdateView):
#
#     model = MonthlyRecord
#     fields = ['vehicle', 'year', 'month', 'fuel_consumed', 'cost', 'km']
#     template_name = 'monthly/edit_monthly.html'
#     form_valid_message = 'Record was successfully updated!'
#     form_invalid_message = 'There are some errors found in form. Please check the data and resubmit.'
#
#     def get_success_url(self):
#         return reverse('records_list')
#
#     def get_context_data(self, **kwargs):
#         context = super(UpdateMonthlyView, self).get_context_data(**kwargs)
#         context['target'] = reverse('edit_record',
#                                     kwargs={'pk': self.get_object().id})
#         return context
#
#
# class MonthlyView(DetailView):
#
#     model = MonthlyRecord
#     template_name = 'monthly/monthly.html'
#

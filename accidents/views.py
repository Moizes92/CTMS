from django.shortcuts import render  # , get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from accidents.models import Accident
from vehicle.models import Vehicle
from accidents.forms import AccidentForm

from django.db.models import Avg, Sum

from braces.views import LoginRequiredMixin, FormMessagesMixin


class AccidentsListView(ListView):

    model = Accident
    template_name = 'accidents/accidents_list.html'


class CreateAccidentView(FormMessagesMixin, CreateView):

    model = Accident
    form_class = AccidentForm
    template_name = 'accidents/add_accident.html'
    form_valid_message = "Accident Record created successfully"
    form_invalid_message = "Some errors were detected during form submission. Please check and resubmit"

    def get_success_url(self):
        return reverse('accidents_list')

    def get_context_data(self, **kwargs):
        context = super(CreateAccidentView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_accident')

        return context


class UpdateAccidentView(FormMessagesMixin, UpdateView):

    model = Accident
    form_class = AccidentForm
    template_name = 'accidents/edit_accident.html'
    form_valid_message = "Accident Record updated successfully"
    form_invalid_message = "Some errors were detected during form submission. Please check and resubmit"

    def get_success_url(self):
        return reverse('accidents_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateAccidentView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_accident', kwargs={'pk': self.get_object().id})
        return context


class DeleteAccidentView(FormMessagesMixin, DeleteView):
    model = Accident
    success_url = reverse_lazy('accidents_list')
    form_valid_message = "Accident Record has been deleted successfully from the database"


class AccidentView(DetailView):

    model = Accident
    template_name = 'accidents/accident.html'


def accidentsView(request, pk):
    accidents_list = Accident.objects.all().filter(id=pk).order_by('-date')
    vehicle = Vehicle.objects.get(id=pk).plate_num
    sum_cost = Accident.objects.filter(id=pk).aggregate(value_sum=Sum('cost'))
    context = dict(
        pk=pk,
        vehicle=vehicle,
        accidents_list=accidents_list,
        sum_cost=sum_cost['value_sum'],
    )
    return render(request, 'accidents/accidents.html', context)

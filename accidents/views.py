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

from django.db.models import Avg, Sum

from braces.views import LoginRequiredMixin


class AccidentsListView(ListView):

    model = Accident
    fields = ['vehicle', 'driver', 'date', 'cost',
              'description', 'image']
    template_name = 'accidents/accidents_list.html'


class CreateAccidentView(CreateView):

    model = Accident
    fields = ['vehicle', 'driver', 'date', 'cost',
              'description', 'image']
    template_name = 'accidents/edit_accident.html'

    def get_success_url(self):
        return reverse('accidents_list')

    def get_context_data(self, **kwargs):
        context = super(CreateAccidentView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_accident')

        return context


class UpdateAccidentView(UpdateView):

    model = Accident
    fields = ['vehicle', 'driver', 'date', 'cost',
              'description', 'image']
    template_name = 'accidents/edit_accident.html'

    def get_success_url(self):
        return reverse('accidents_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateAccidentView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_accident',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteAccidentView(DeleteView):
    model = Accident
    success_url = reverse_lazy('accidents_list')


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

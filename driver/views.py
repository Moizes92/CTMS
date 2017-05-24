from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Driver

from braces.views import LoginRequiredMixin


class DriverListView(ListView):

    model = Driver
    fields = ['plate_num', 'current_driver']
    template_name = 'drivers/drivers_list.html'


class CreateDriverView(CreateView):

    model = Driver
    fields = ['first_name', 'last_name', 'email', 'license_category',
              'license_renewal_date', 'image']
    template_name = 'drivers/edit_driver.html'

    def get_success_url(self):
        return reverse('drivers_list')

    def get_context_data(self, **kwargs):
        context = super(CreateDriverView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_driver')

        return context


class UpdateDriverView(UpdateView):

    model = Driver
    fields = ['first_name', 'last_name', 'email', 'license_category',
              'license_renewal_date', 'image']
    template_name = 'drivers/edit_driver.html'

    def get_success_url(self):
        return reverse('drivers_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateDriverView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_driver',
                                    kwargs={'pk': self.get_object().id})
        return context


class DeleteDriverView(DeleteView):
    model = Driver
    success_url = reverse_lazy('drivers_list')


class DriverView(DetailView):

    model = Driver
    template_name = 'drivers/driver.html'

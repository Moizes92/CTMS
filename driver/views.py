from django.core.urlresolvers import reverse, reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from driver.models import Driver
from driver.forms import DriverForm

from braces.views import LoginRequiredMixin, FormMessagesMixin
from django_popup_view_field.registry import registry_popup_view


class DriverListView(ListView):

    model = Driver
    template_name = 'drivers/drivers_list.html'


class CreateDriverView(FormMessagesMixin, CreateView):

    extra_context = {'object_name': _(u'Driver')}
    model = Driver
    form_class = DriverForm
    template_name = 'drivers/add_driver.html'
    form_valid_message = 'Driver was successfully Created!'
    form_invalid_message = 'There are some errors found in form. Please check the data and resubmit.'

    def get_success_url(self):
        return reverse('drivers_list')

    def get_context_data(self, **kwargs):
        context = super(CreateDriverView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_record')
        return context


class UpdateDriverView(UpdateView):

    model = Driver
    form_class = DriverForm
    template_name = 'drivers/edit_driver.html'

    def get_success_url(self):
        return reverse('drivers_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateDriverView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_driver', kwargs={'pk': self.get_object().id})
        return context


class DeleteDriverView(FormMessagesMixin, DeleteView):

    model = Driver
    template_name = 'drivers/driver_confirm_delete.html'
    success_url = reverse_lazy('drivers_list')
    form_valid_message = 'Driver was deleted successfully!'



class DriverView(DetailView):

    model = Driver
    template_name = 'drivers/driver.html'

registry_popup_view.register(DeleteDriverView)
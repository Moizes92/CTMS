from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, DetailView,)

from gpsdevices.models import GPSDevice
from gpsdevices.forms import GPSDeviceForm

from braces.views import LoginRequiredMixin, FormMessagesMixin


class GPSDeviceListView(ListView):

    model = GPSDevice
    template_name = 'gpsdevice/gpsdevices_list.html'


class CreateGPSDeviceView(FormMessagesMixin, CreateView):

    extra_context = {'object_name': _(u'GPSDevice')}
    model = GPSDevice
    template_name = 'gpsdevice/add_gpsdevice.html'
    form_class = GPSDeviceForm
    template_name = 'gpsdevice/add_gpsdevice.html'
    form_valid_message = 'GPS Device was successfully added!'
    form_invalid_message = 'Some errors were found during form submission. Please check the data and resubmit.'

    def get_success_url(self):
        return reverse('gpsdevices_list')

    def get_context_data(self, **kwargs):
        context = super(CreateGPSDeviceView, self).get_context_data(**kwargs)
        context['target'] = reverse('add_gpsdevice')

        return context


class UpdateGPSDeviceView(FormMessagesMixin, UpdateView):

    model = GPSDevice
    form_class = GPSDeviceForm

    template_name = 'gpsdevice/edit_gpsdevice.html'
    form_valid_message = 'Device records updated successfully'

    def get_success_url(self):
        return reverse('gpsdevices_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateGPSDeviceView, self).get_context_data(**kwargs)
        context['target'] = reverse('edit_gpsdevice', kwargs={'pk': self.get_object().id})
        return context


class DeleteGPSDeviceView(DeleteView):
    model = GPSDevice
    success_url = reverse_lazy('gpsdevices_list')


class GPSDeviceView(DetailView):

    model = GPSDevice
    template_name = 'gpsdevice/gpsdevice.html'


def view_gpsdevice(request, pk):
    
    gpsdevice = GPSDevice.objects.get(id=pk)
    context = dict(
        gpsdevice=gpsdevice,
    )
    return render(request, 'gpsdevice/view_gpsdevice.html', context)

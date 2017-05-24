from django.conf.urls import url
from django.contrib.auth import views as auth_views
from authentication import views as views
from vehicle import views as v_views
from driver import views as d_views
from accidents import views as a_views
from django.views.generic import TemplateView
from reporting import views as r_views

urlpatterns = [
   url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
   url(r'^home$', views.index, name='index'),
   url(r'^location$', views.location, name='location'),
   url(r'^route$', views.route, name='routes'),
   url(r'^report$', views.report, name='reports'),
   url(r'^asset$', views.asset, name='assets'),
   url(r'^schedule$', views.schedule, name='schedules'),

   url(r'^vehicles/$', v_views.VehicleListView.as_view(), name='vehicles_list'),
   url(r'^add_vehicle/$', v_views.CreateVehicleView.as_view(), name='add_vehicle'),
   url(r'^edit_vehicle/(?P<pk>\d+)/$', v_views.UpdateVehicleView.as_view(), name='edit_vehicle'),
   url(r'^vehicle/(?P<pk>\d+)/$', v_views.VehicleView.as_view(), name='vehicle'),
   url(r'^view_vehicle/(?P<pk>\d+)/$', v_views.view_vehicle, name='view_vehicle'),

   url(r'^drivers_list/$', d_views.DriverListView.as_view(), name='drivers_list'),
   url(r'^add_driver/$',d_views.CreateDriverView.as_view(), name='add_driver'),
   url(r'^edit_driver/(?P<pk>\d+)/$', d_views.UpdateDriverView.as_view(), name='edit_driver'),
   url(r'^driver/(?P<pk>\d+)/$', d_views.DriverView.as_view(), name='view_driver'),

   url(r'^accidents_list/$', a_views.AccidentsListView.as_view(), name='accidents_list'),
   url(r'^add_accident/$', a_views.CreateAccidentView.as_view(), name='add_accident'),
   url(r'^edit_accident/(?P<pk>\d+)/$', a_views.UpdateAccidentView.as_view(), name='edit_accident'),
   url(r'^delete_accident/(?P<pk>\d+)/$', a_views.DeleteAccidentView.as_view(), name='delete_accident'),
   url(r'^accident/(?P<pk>\d+)/$', a_views.AccidentView.as_view(), name='view_accident'),
   url(r'^accidents/(?P<pk>\d+)/$', a_views.accidentsView, name='accidents'),

   url(r'^records_list/$', r_views.MonthlyListView.as_view(), name='records_list'),
   url(r'^add_record/$', r_views.CreateMonthlyView.as_view(), name='add_record'),
   url(r'^edit_record/(?P<pk>\d+)/$', r_views.UpdateMonthlyView.as_view(), name='edit_record'),
   url(r'^record/(?P<pk>\d+)/$', r_views.MonthlyView.as_view(), name='view_record'),
]

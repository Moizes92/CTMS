from django.shortcuts import render
from django.contrib.auth import authenticate, login


def index(request):
	return render(request, "index.html")


def location(request):
    return render(request, "tracking/location.html")

def route(request):
	return render(request, "routes.html")

def vehicle(request):
	return render(request, "vehicles_list.html")

def report(request):
	return render(request, "reports.html")

def asset(request):
	return render(request, "gpsdevice/gpsdevice.html")

def schedule(request):
	return render(request, "schedules.html")


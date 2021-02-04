from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def test(request, *arg, **kwargs):
	return HttpResponse('OK')

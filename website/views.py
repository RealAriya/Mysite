from django.shortcuts import render

from django.http import HttpResponse,JsonResponse


def http_test(request):
    return HttpResponse('hello')

def json_test(request):
    return JsonResponse({'name': 'Arya', 'family-name':'Tahmasebi'})

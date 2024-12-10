# mysite/middleware.py
from django.shortcuts import render

class ComingSoonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = render(request, 'coming-soon.html')
        return response


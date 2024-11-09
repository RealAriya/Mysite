from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import Contact
from website.forms import NameForm,Contact_Form


def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    return render(request,'website/contact.html')



def form_view(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')

    form = Contact_Form()
    return render(request,'test.html',{'form':form})
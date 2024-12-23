from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,Contact_Form,newsletter_Form
from django.contrib import messages


def index_view(request):
    return render(request,'website/index.html')


def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.cleaned_data['name'] = 'Unknown'  
            contact = Contact(**form.cleaned_data)
            contact.save()
            messages.add_message(request, messages.SUCCESS, "Your ticket submited successfully.")
        else:
             messages.add_message(request, messages.ERROR, "Your ticket didn't submited.")

    form = Contact_Form()

    return render(request,'website/contact.html',{'form':form})



def newsletter_view(request):
    if request.method == 'POST':
        form = newsletter_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
    

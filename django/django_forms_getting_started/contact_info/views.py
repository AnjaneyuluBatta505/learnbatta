from .forms import ContactInfoForm
from django.http import HttpResponse
from django.shortcuts import render

def create_contact_info(request):
    if request.method == 'POST':
       form = ContactInfoForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponse("Saved Contact info. Check the database for verification") 
    else:
       form = ContactInfoForm()
    context = {'form': form}
    return render(request, 'template.html', context)

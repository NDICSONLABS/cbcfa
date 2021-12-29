from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FaClerkInformationForm
from .department import DEPARTMENTS

# Create your views here.

def clerk(request):
    
    context = {}
    form  = FaClerkInformationForm()
    if request.method == 'GET':
        context['form'] = form
        return render(request, 'clerk.html', context)

    if request.method == 'POST':
        form  = FaClerkInformationForm(request.POST)
        print(form.is_valid())
        
        if form.is_valid():
            form.save()

            messages.success(request, "Your information was succesfully added")
            return redirect("https://drive.google.com/drive/folders/1na6yGjYI6wbuhWaAZIFDxsH2l7-plfuS?usp=sharing")

    messages.error(request, "Please provide all information")
    return render(request, 'clerk.html', {'form':form})

def download(request):
    id="1iI5DnSlydRvLZLwLueZZ8_JmYPav0Eq_"
    context = {'departments':DEPARTMENTS.items()}
    if request.method == 'GET':
        return render(request, 'download.html', context)

    if request.method == 'POST':
        
        return redirect('download')


    return render(request, 'download.html', context)
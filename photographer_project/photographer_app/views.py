# photographer_app/views.py
from django.shortcuts import render, redirect
from .forms import AddPhotographerForm, SearchPhotographerForm
from .models import Photographer

def add_photographer(request):
    if request.method == 'POST':
        form = AddPhotographerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_all_photographers')
    else:
        form = AddPhotographerForm()
    
    return render(request, 'add_photographer.html', {'form': form})

def search_photographer(request):
    if request.method == 'POST':
        form = SearchPhotographerForm(request.POST)
        if form.is_valid():
            search_option = form.cleaned_data['search_option']
            search_key = form.cleaned_data['search_key']
            
            if search_option == 'business_name':
                photographers = Photographer.objects.filter(business_name__icontains=search_key)
            elif search_option == 'photographer_name':
                # Assuming photographer_name is a field in the model
                photographers = Photographer.objects.filter(photographer_name__icontains=search_key)
            elif search_option == 'event':
                photographers = Photographer.objects.filter(events_covered__icontains=search_key)
            
            return render(request, 'search_photographer_result.html', {'photographers': photographers})
    else:
        form = SearchPhotographerForm()

    return render(request, 'search_photographer.html', {'form': form})

def show_all_photographers(request):
    photographers = Photographer.objects.all()
    return render(request, 'show_all_photographers.html', {'photographers': photographers})


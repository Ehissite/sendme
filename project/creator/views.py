from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Creators
from .forms import CreatorForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('creator:login')
    else:    
       form = UserCreationForm()
    return render(request, 'core/signup.html', {
        'form': form,
    })
    
def creator(request, pk):
    creator = Creators.objects.get(pk=pk)
    return render(request, 'core/creator.html', {
        'creator': creator,
    })

@login_required
def myaccountpage(request):
    creator = request.user.creator
    return render(request, 'core/myaccountpage.html', {
        'creator': creator,
     })
     
def creators(request):
    # get creators from database
       creators = Creators.objects.all()
       return render(request, 'core/creators.html', {
        'creators': creators,
    })
       
def edit(request):
    # because a creator is not created instantly, we are trying the creator request(where true, an instance of the 
    # creator is passed i.e the data else a form is presented to the user)
    try:
        creator = request.user.creator
        # incase the user wants to update the form (instance=creator fills out the info)
        if request.method == "POST":
            form = CreatorForm(request.POST, request.FILES, instance=creator)
            
            if form.is_valid():
                form.save()
                
                return redirect('app:index')
        else:
            form = CreatorForm(instance=creator)
            
    except Exception:
        if request.method == "POST":
            form = CreatorForm(request.POST, request.FILES)
            
            if form.is_valid():
                creator = form.save(commit=False) # it would not be stored in the database
                creator.user = request.user
                creator.save()
                
                return redirect('app:index')
    
        else:
            form = CreatorForm()
            
    return render(request, 'core/edit.html', {
       'form': form, 
    })
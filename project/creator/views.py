from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

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
 
def creators(request):
    # get creators from database
    
       return render(request, 'core/creators.html', {
        # 'form': form,
    })
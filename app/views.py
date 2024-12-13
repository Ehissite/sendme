from django.shortcuts import render, redirect
from creator.models import Creators

def index(request):
    creators = Creators.objects.all()
    if request.user.is_authenticated:
        try:
            creator = request.user.creator
        except:
            return redirect('creator:edit')
    return render(request, 'core/index.html', {
        'creators': creators,
    })

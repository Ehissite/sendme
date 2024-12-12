# importing ModelForm from django to handle forms
from django.forms import ModelForm
from .models import Creators

class CreatorForm(ModelForm):
    class Meta:
        model = Creators
        fields = ('title','description','image',)
    
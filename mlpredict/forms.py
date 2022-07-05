from django.forms import ModelForm
from .models import features

class medicalForm(ModelForm):    
    class Meta:
        model = features
        fields = ["Age","sex","bmi","children","smoker","region"]

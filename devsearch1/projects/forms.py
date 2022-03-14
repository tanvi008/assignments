from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description','demo_link','source_link','tags'] 
        #wrote here all so that all the fields from Project class will be created automatically except for the id and created

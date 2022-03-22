from django import forms
from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description','demo_link','source_link','tags'] 
        #wrote here all so that all the fields from Project class will be created automatically except for the id and created
        widgets ={    
            'tags':forms.CheckboxSelectMultiple(),
        }


    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # We are doing the below things so that we can input into the different fields of the form

        for k, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input'})
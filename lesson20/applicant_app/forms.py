from django import forms
from .models import *


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name_vacancy', 'name', 'surname', 'middle_name', 'date_born', 'email', 'skills',
                  'professional_experience', 'education']
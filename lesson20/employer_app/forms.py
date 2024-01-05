from django import forms
from .models import *


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['name_vacancy', 'name_company', 'salary', 'required_skills', 'responsibilities', 'address']

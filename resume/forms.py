from django import forms
from django.forms import formset_factory

from .models import Institution


# creating a form
class ResumeForm(forms.Form):
    name = forms.CharField(required= True)
    email = forms.CharField(required= True)
    phone = forms.IntegerField(required= True)
    image= forms.ImageField()
    linked_in= forms.CharField()
    github=forms.CharField()



class SkillForm(forms.Form):
    skill_name = forms.CharField()
    level=forms.IntegerField()

class ExperienceForm(forms.Form):
    experience_name =forms.CharField()
    position= forms.CharField()
    years= forms.FloatField()


class InstitutionForm(forms.Form):
    institution = forms.CharField()
    result= forms.FloatField()

InstitutionFormSet = formset_factory(InstitutionForm, extra=2)

formset = InstitutionFormSet()
for form in formset:
     print(form.as_table())


from django.http import HttpResponse, response
from django.shortcuts import render
from .forms import ResumeForm,SkillForm,InstitutionForm,ExperienceForm,InstitutionFormSet
from django.views.generic.edit import FormView
from django.forms import formset_factory



# Create your views here.
def resume_home(request):
    return render(request,'resume/home.html')


# def resume_form(request):
#     # res= ResumeForm()
#     # skill= SkillForm()
#     # exp= ExperienceForm()
#     # inst= InstitutionForm()
#     # context = {
#     #     "res":res,
#     #     'inst': inst,
#     #     'skill':skill,
#     #     'exp': exp,
#     #
#     # }
#     #
#     return render(request,'resume/resume_form.html',context)


def resume_form(request):
    InstitutionFormSet = formset_factory(InstitutionForm)
    if request.method == 'POST':
        formset = InstitutionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = InstitutionFormSet()
    return render('resume/resume_form.html', {'formset': formset})

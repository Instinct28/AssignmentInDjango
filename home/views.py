from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from home.models import study

# Create your views here.
def index(request):
    if request.method == 'GET' or request.method == 'POST':
        studies = study.objects.all().values()  
        studies_list = list(studies)  
        context = {
        'title': 'Study Table',
        'study_data': studies_list
        }
    return render(request, 'index.html', context)

def addStudy(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phase = request.POST.get('phase')
        sponsorName = request.POST.get('sponsorName')
        description = request.POST.get('description')
        Study = study(name = name, description = description, phase = phase, sponsorName = sponsorName)
        Study.save()
        return redirect('/')
    return render(request, 'addStudy.html')

def updateStudy(request, id):
    study_instance = get_object_or_404(study, id=id)
    if request.method == 'POST':
        study_instance.name = request.POST.get('name')
        study_instance.phase = request.POST.get('phase')
        study_instance.sponsorName = request.POST.get('sponsorName')
        study_instance.description = request.POST.get('description')
        study_instance.save()  
        return redirect('/')  
    return render(request, 'updateStudy.html', {'study': study_instance})

def viewStudy(request, id):
    Study = get_object_or_404(study, id=id)
    context = {
        'study': Study
    }
    return render(request, 'viewStudy.html', context)

def deleteStudy(request):
    if request.method == 'POST':
        studies_to_delete = request.POST.getlist('studies_to_delete')
        if studies_to_delete:
            study.objects.filter(id__in=studies_to_delete).delete()
        return redirect('/')
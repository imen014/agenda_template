from django.shortcuts import render, get_object_or_404, redirect
from agenda_management_app.forms import AgendaForm
from agenda_management_app.models import Agenda


def create_agenda(request):
    agenda_form = AgendaForm()
    return render(request, 'agenda_management_app/agendas/create.html',{'agenda_form':agenda_form})


def save_agenda(request):
    agenda_form = AgendaForm()
    message = ""
    if request.method == "POST":
        agenda_form = AgendaForm(request.POST)
        if agenda_form.is_valid():
            agenda_form.save()
            message = "agenda saved succefully"
            return render(request, 'agenda_management_app/agendas/created.html', {'message':message})
        else:
            message = "agenda can't be saved"
            return render(request, 'agenda_management_app/agendas/created.html', {'message':message})
        
def get_agendas(request):
    agendas = Agenda.objects.all()
    return render(request, 'agenda_management_app/agendas/all_agendas.html', {'agendas':agendas})

def delete_all_agendas(request):
    agendas = Agenda.objects.all()
    message=""
    agendas.delete()
    message="agendas deleted succefully"
    return render(request, 'agenda_management_app/agendas/agendas_deleted.html', {'message':message})


def update_agenda(request, id):
    agenda = get_object_or_404(Agenda,id=id)
    agenda_form = AgendaForm(instance=agenda)
    message = ""
    if request.method == "POST":
        agenda_form = AgendaForm(request.POST, instance=agenda)
        agenda_form.save()
        message = "agenda updated succefully"
        return redirect('get_agendas')
    else:
        message = "agenda can't be updated"
        return render(request, 'agenda_management_app/agendas/agendas_updated.html', {'message':message})

def edit_agenda(request, id):
    agenda = get_object_or_404(Agenda,id=id)
    agenda_form = AgendaForm(instance=agenda)
    return render(request, 'agenda_management_app/agendas/edit_agenda.html',{'agenda_form':agenda_form,'agenda':agenda})


def delete_agenda(request, id):
    agenda = get_object_or_404(Agenda,id=id)
    agenda.delete()
    return redirect('get_agendas')



     
    
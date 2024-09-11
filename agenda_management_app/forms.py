from django.forms import ModelForm
from agenda_management_app.models import Agenda


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = ['contact_name','contact_number']

      
from ..models import Paciente

def get_pacientes():
    pacientes = Paciente.objects.all()
    return pacientes

def get_paciente(pac_pk):
    paciente = Paciente.objects.get(pk=pac_pk)
    return paciente

def create_paciente(pac):
    paciente = Paciente(name=pac["name"])
    paciente.save()
    return paciente

def update_paciente(pac_pk, new_pac):
    paciente = get_paciente(pac_pk)
    paciente.name = new_pac["name"]
    paciente.save()
    return paciente


import requests
from paciente.models import ResultadoEEG, Paciente
from datetime import datetime

def procesar_eeg_para_paciente(paciente_id):
    paciente = Paciente.objects.get(pk=paciente_id)
    eeg_id = paciente.id  # o puedes usar un UUID aleatorio si prefieres

    response = requests.post("http://localhost:8001/analyze-eeg/", json={"eeg_id": eeg_id})

    if response.status_code == 200:
        data = response.json()
        resultado = ResultadoEEG.objects.create(
            paciente=paciente,
            eeg_id=data["eeg_id"],
            diagnosis=data["diagnosis"],
            confidence=data["confidence"],
            timestamp=datetime.fromisoformat(data["timestamp"])
        )
        return resultado
    else:
        raise Exception("Error al procesar el EEG")

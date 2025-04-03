from django.shortcuts import render
from .logic import pacientes_logic as pl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def pacientes_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            paciente_dto = pl.get_paciente(id)
            paciente = serializers.serialize('json', [paciente_dto,])
            return HttpResponse(paciente, 'application/json')
        else:
            pacientes_dto = pl.get_pacientes()
            pacientes = serializers.serialize('json', pacientes_dto)
            return HttpResponse(pacientes, 'application/json')
    if request.method == 'POST':
        paciente.dto = pl.create_paciente(json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
@csrf_exempt
def paciente_view(request,pk):
    if request.method == 'GET':
        paciente_dto = pl.get_paciente(pk)
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    
    if request.method == 'PUT':
        paciente_dto = pl.update_paciente(pk, json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    
from django.http import JsonResponse
from paciente.eeg.eeg_service import procesar_eeg_para_paciente
@csrf_exempt
def analizar_eeg_view(request, paciente_id):
    try:
        resultado = procesar_eeg_para_paciente(paciente_id)
        return JsonResponse({
            "message": "EEG procesado",
            "diagnosis": resultado.diagnosis,
            "confidence": resultado.confidence,
            "timestamp": resultado.timestamp
        })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

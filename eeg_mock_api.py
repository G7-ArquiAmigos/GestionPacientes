# eeg_mock_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from random import choice, uniform
from time import sleep
from datetime import datetime

app = FastAPI()

class EEGRequest(BaseModel):
    eeg_id: int

@app.post("/analyze-eeg/")
async def analyze_eeg(request: EEGRequest):
    sleep(uniform(0.5, 1.5))  # simula procesamiento
    diagnosis = choice(["Normal", "Posible crisis epiléptica", "Anomalía no concluyente"])
    return {
        "eeg_id": request.eeg_id,
        "diagnosis": diagnosis,
        "confidence": round(uniform(70.0, 99.9), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

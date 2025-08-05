from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

class DadosLicenca(BaseModel):
    email: str
    chave: str

@app.post("/validar")
def validar(dados: DadosLicenca):
    try:
        email = dados.email.lower()
        chave = dados.chave

        # 🔍 Consulta via API REST do Supabase
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/licencas?email=eq.{email}&chave=eq.{chave}",
            headers=HEADERS
        )

        if response.status_code == 200 and response.json():
            return {"status": "validado"}
        else:
            return {"status": "invalido"}

    except Exception as e:
        return {"erro": str(e)}

@app.get("/")
def index():
    return {"mensagem": "API LuxTrader está online"}

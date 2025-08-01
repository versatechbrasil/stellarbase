from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

licencas = {
    "cliente1@gmail.com": "ABC123-XYZ456",
    "cliente2@teste.com": "XYZ999-AAA000"
}

class DadosLicenca(BaseModel):
    email: str
    chave: str

@app.post("/validar")
def validar(dados: DadosLicenca):
    if licencas.get(dados.email.lower()) == dados.chave:
        return {"status": "validado"}
    return {"status": "invalido"}

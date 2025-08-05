from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# 🔐 Dados de conexão com o Supabase
SUPABASE_URL = "postgresql://postgres:Ltx#93fP!rZq7sWd@db.vtedtjaggqajirelkcsi.supabase.co:5432/postgres"

# 📌 Conexão única
conn = psycopg2.connect(SUPABASE_URL)
cursor = conn.cursor()

class DadosLicenca(BaseModel):
    email: str
    chave: str

@app.post("/validar")
def validar(dados: DadosLicenca):
    try:
        cursor.execute("SELECT chave FROM licencas WHERE email = %s", (dados.email.lower(),))
        resultado = cursor.fetchone()

        if resultado and resultado[0] == dados.chave:
            return {"status": "validado"}
        else:
            return {"status": "invalido"}

    except Exception as e:
        return {"erro": str(e)}

@app.get("/")
def index():
    return {"mensagem": "API LuxTrader está online"}

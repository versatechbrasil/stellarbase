import requests

url = "https://luxtrader-licenca-api.onrender.com/validar"  # Substitua com seu link real

dados = {
    "email": "cliente1@gmail.com",
    "chave": "ABC123-XYZ456"
}

resposta = requests.post(url, json=dados)

print("Status:", resposta.status_code)
print("Retorno:", resposta.json())

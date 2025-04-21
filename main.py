from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo para entrada de dados
class Operacao(BaseModel):
    a: float
    b: float

@app.post("/somar")
def somar(valores: Operacao):
    return {"resultado": valores.a + valores.b}

@app.post("/subtrair")
def subtrair(valores: Operacao):
    return {"resultado": valores.a - valores.b}

@app.post("/multiplicar")
def multiplicar(valores: Operacao):
    return {"resultado": valores.a * valores.b}

@app.post("/dividir")
def dividir(valores: Operacao):
    if valores.b == 0:
        return {"erro": "Divisão por zero não é permitida"}
    return {"resultado": valores.a / valores.b}

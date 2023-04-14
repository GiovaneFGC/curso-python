import sqlite3

from typing import Optional, Text

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class cliente (BaseModel):
    cpf: str
    nome: str
    email: str
    valor: str

def score():
    c = sqlite3.connect('/Users/Ijovem01/coursepython/database/tatoo.db')
    cr = c.cursor()
    cr.execute("""select cpf , sum(valor) from clientes group by cpf""")
    lista=cr.fetchall()
    c.close()
    return dict(lista)

@app.post("/gravar")
def gravar(c: cliente):
    msg = "Gracias Sr/Sra seu CPF está inválido: " + c.nome + " " + c.cpf
    return {"msg": msg}

@app.put("/atualizar")
def atualizar(c: cliente):
    msg = "Gracias Sr/Sra seus dados foram atualizados com sucesso: " + c.nome + " " + c.cpf
    return {"msg": msg}

@app.delete("/excluir")
def excluir(cpf: str, nome: str):
    msg = "Gracias Sr/Sra seus dados foram excluidos com sucesso: "
    return {"msg": msg}

@app.get("/listar_clientes")
def listar_clientes():
    return {"Hello": "World"}

@app.get("/listar_score")
def listar_score():
    return score()

@app.get("/listar_unico")
def listar_unico(cpf: str):
    msg = "aqui está o cliente: "
    return {"msg": cpf}

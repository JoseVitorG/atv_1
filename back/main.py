from fastapi import FastAPI, Query # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
import uvicorn # type: ignore
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["*"]
)

partidas = [
    {"partida": "gremio x inter"},
    {"partida": "gremio x bahia"},
    {"partida": "gremio x flamengo"},
    {"partida": "gremio x juventos"},
    {"partida": "juventos x inter"},
    {"partida": "juventos x bahia"},
    {"partida": "juventos x flamengo"},
    {"partida": "flamengo x inter"},
]

@app.get("/pegar_data")
async def get_data():    
  return partidas

@app.get("/pegar_time")
async def get_data(nome: str = Query(...)):
    data = []
    for item in partidas:
        if re.search(nome, item['partida'], re.IGNORECASE):
            data.append(item)
    return data if data else 'nada encontrado'

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=3000)

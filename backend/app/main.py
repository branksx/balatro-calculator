from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from backend.app.routers import hands
from .database import SessionLocal
from .routers import calculations, hands

app = FastAPI(
    title="Balatro Hand Calculator API",
    description="API backend para cálculo de pontuações de mão de balatro",
    version="0.1.0",
    )

# Configuração do CORS (Permite que qualquer frontend acesse a API durante o desenvolvimento)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens (apenas para desenvolvimento)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Registrar o router de cálculos
app.include_router(calculations.router)
app.include_router(hands.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de cálculo de pontuações de mão de balatro!"}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db :=SessionLocal)):
    try:
        #Testa a ligação contando quantas mãos existem  na tabela que validamos
        total_hands = db.execute(text("SELECT COUNT(*) FROM TB_POKER_HANDS")).scalar()
        return{
            "status": "Successo",
            "mensagem": "Ligação ao SQL Server Express realizada com sucesso!",
            "total_hands": total_hands
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao conectar ao banco de dados: {str(e)}")
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Jokers, JokerEffects
from ..schemas import JokerResponse, JokerEffectResponse

router = APIRouter(prefix="/jokers", tags=["Jokers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[JokerResponse])
def get_all_jokers(db: Session = Depends(get_db)):
    """Retorna todos os jokers cadastrados na base de dados ordenados por ID."""
    jokers = db.query(Jokers).order_by(Jokers.id).all()
    return jokers

@router.get("/{joker_id}", response_model=JokerResponse)
def get_joker_by_id(joker_id: int, db: Session = Depends(get_db)):
    """Retorna os detalhes de um joker específico pelo seu ID."""
    joker = db.query(Jokers).filter(Jokers.id == joker_id).first()
    if not joker:
        raise HTTPException(status_code=404, detail="Joker não encontrado.")
    return joker

@router.get("/{joker_id}/effects", response_model=list[JokerEffectResponse])
def get_joker_effects(joker_id: int, db: Session = Depends(get_db)):
    """Retorna todos os efeitos de um joker específico pelo seu ID."""
    effects = db.query(JokerEffects).filter(JokerEffects.joker_id == joker_id).all()
    if not effects:
        raise HTTPException(status_code=404, detail="Nenhum efeito encontrado para este joker.")
    return effects
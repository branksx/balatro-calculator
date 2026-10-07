from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import SessionLocal
from ..models import PokerHand
from ..schemas import PokerHandResponse  # <-- Importante: usar o schema correto

router = APIRouter(prefix="/hands", tags=["Poker Hands"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[PokerHandResponse])
def get_all_hands(db: Session = Depends(get_db)):
    """Retorna todas as mãos de póquer cadastradas na base de dados ordenadas por ID."""
    hands = db.query(PokerHand).order_by(PokerHand.id).all()
    return hands

@router.get("/{hand_id}", response_model=PokerHandResponse)
def get_hand_by_id(hand_id: int, db: Session = Depends(get_db)):
    """Retorna os detalhes de uma mão específica pelo seu ID."""
    hand = db.query(PokerHand).filter(PokerHand.id == hand_id).first()
    if not hand:
        raise HTTPException(status_code=404, detail="Mão de póquer não encontrada.")
    return hand
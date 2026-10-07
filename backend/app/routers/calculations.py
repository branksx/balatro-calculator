from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import PokerHand
from ..schemas import HandCalculateRequest, HandCalculateResponse

router = APIRouter(prefix="/calculate", tags=["Calculation Engine"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=HandCalculateResponse)
def calculate_hand_score(payload: HandCalculateRequest, db: Session = Depends(get_db)):
    # 1. Buscar a mão no banco de dados
    hand = db.query(PokerHand).filter(PokerHand.id == payload.hand_id).first()
    if not hand:
        raise HTTPException(status_code=404, detail="Mão de póquer não encontrada.")
    
    # 2. Aplicar a regra de progressão matemática que testámos no SQL:
    # Chips = base_chip + ((level - base_level) * up_chip)
    # Multi = base_multi + ((level - base_level) * up_multi)
    level_diff = payload.level - hand.hand_base_level
    
    calc_chips = hand.hand_base_chip + (level_diff * hand.hand_up_chip)
    calc_multi = hand.hand_base_multi + (level_diff * hand.hand_up_multi)
    
    # Pontuação final básica em Balatro = Chips * Mult
    score = calc_chips * calc_multi

    return {
        "hand_id": hand.id,
        "hand_name": hand.hand_name,
        "level": payload.level,
        "calculated_chips": calc_chips,
        "calculated_multi": calc_multi,
        "score": score
    }
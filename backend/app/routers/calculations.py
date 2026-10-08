from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import PokerHand, JokerEffects
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
    
    chips_atual = hand.hand_base_chip + (level_diff * hand.hand_up_chip)
    multi_atual = hand.hand_base_multi + (level_diff * hand.hand_up_multi)
    
    for j_id in payload.joker_ids:
        # Buscamos no banco os efeitos pertencentes a este Joker:
        effects = db.query(JokerEffects).filter(JokerEffects.joker_id == j_id).all()
        
        # Percorremos cada efeito encontrado para aplicar:
        for effect in effects:
            valor = float(effect.effect_value)
            tipo = effect.effect_type.strip().upper()
            
            if tipo in ("ADD_CHIP", "ADD_CHIPS", "+CHIP", "+CHIPS"):
                chips_atual += int(valor)
            elif tipo in ("ADD_MULTI", "ADD_MULT", "+MULTI", "+MULT"):
                multi_atual += int(valor)
            elif tipo in ("X_MULTI", "X_MULT", "XMULTI", "XMULT", "*MULTI"):
                multi_atual *= valor
            # Pontuação final básica em Balatro = Chips * Mult
            score = int(chips_atual * multi_atual)

    return {
        "hand_id": hand.id,
        "hand_name": hand.hand_name,
        "level": payload.level,
        "calculated_chips": chips_atual,
        "calculated_multi": multi_atual,
        "joker_ids": payload.joker_ids,
        "score": score
    }
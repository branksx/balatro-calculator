from pydantic import BaseModel, Field

class HandCalculateRequest(BaseModel):
    hand_id: int = Field(..., description="The ID of the poker hand to calculate.")
    level: int = Field(..., description="The level of the poker hand.")
    joker_ids: list[int] = Field(default=[], description="Lista de IDs dos Jokers selecionados.")

class HandCalculateResponse(BaseModel):
    hand_id: int
    hand_name: str
    level: int
    calculated_chips: int
    calculated_multi: int
    joker_ids: list[int] = []
    score: int
    
    class Config:
        from_attributes = True # Permite que o Pydantic converta automaticamente os atributos do modelo SQLAlchemy para o modelo Pydantic.
        
class PokerHandResponse(BaseModel):
    id: int
    hand_name: str
    hand_base_level: int
    hand_base_chip: int
    hand_base_multi: int
    hand_up_chip: int
    hand_up_multi: int

    class Config:
        from_attributes = True  # Permite que o Pydantic leia diretamente dos modelos SQLAlchemy.
        
class JokerResponse(BaseModel):
    id: int
    joker_name: str
    joker_rarity: str
    joker_description: str

    class Config:
        from_attributes = True  # Permite que o Pydantic leia diretamente dos modelos SQLAlchemy.
        
class JokerEffectResponse(BaseModel):
    id: int
    joker_id: int
    effect_type: str
    effect_value: str
    condition_type: str
    is_pre_calc: int  # 0 = False, 1 = True

    class Config:
        from_attributes = True  # Permite que o Pydantic leia diretamente dos modelos SQLAlchemy.
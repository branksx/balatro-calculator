from pydantic import BaseModel, Field

class   HandCalculateRequest(BaseModel):
    hand_id: int = Field(..., description="The ID of the poker hand to calculate.")
    level: int = Field(..., description="The level of the poker hand.")

class HandCalculateResponse(BaseModel):
    hand_id: int
    hand_name: str
    level: int
    calculated_chips: int
    calculated_multi: int
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
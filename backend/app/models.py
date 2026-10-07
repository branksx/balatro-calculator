from sqlalchemy import Column, Integer, String, BigInteger
from .database import Base

class PokerHand(Base):
    __tablename__ = "TB_POKER_HANDS"

    id = Column(Integer, primary_key=True, index=True)
    hand_name = Column(String(50), nullable=False)
    hand_base_level = Column(BigInteger, nullable=False)
    hand_base_chip = Column(BigInteger, nullable=False)
    hand_base_multi =  Column(BigInteger, nullable=False)
    hand_up_chip = Column(BigInteger, nullable=False)
    hand_up_multi = Column(BigInteger, nullable=False)
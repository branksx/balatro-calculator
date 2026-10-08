from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey
from .database import Base

class PokerHand(Base):
    __tablename__ = "TB_POKER_HANDS"

    id = Column("ID", Integer, primary_key=True, index=True)
    hand_name = Column("HAND_NAME", String(50), nullable=False)
    hand_base_level = Column("HAND_BASE_LEVEL", BigInteger, nullable=False)
    hand_base_chip = Column("HAND_BASE_CHIP", BigInteger, nullable=False)
    hand_base_multi =  Column("HAND_BASE_MULTI", BigInteger, nullable=False)
    hand_up_chip = Column("HAND_UP_CHIP", BigInteger, nullable=False)
    hand_up_multi = Column("HAND_UP_MULTI", BigInteger, nullable=False)

class Jokers(Base):
    __tablename__ = "TB_JOKERS"
    id = Column("ID", Integer, primary_key=True, index=True)
    joker_name = Column("JOKER_NAME", String(50), nullable=False)
    joker_rarity = Column("JOKER_RARITY", String(25), nullable=False)
    joker_description = Column("JOKER_DESCRIPTION", String(125), nullable=False)

class JokerEffects(Base):
    __tablename__ = "TB_JOKER_EFFECTS"
    id = Column("ID", Integer, primary_key=True, index=True)
    joker_id = Column("JOKER_ID", Integer, ForeignKey("TB_JOKERS.ID"), nullable=False)
    effect_type= Column("EFFECT_TYPE", String(25), nullable=False)
    effect_value = Column("EFFECT_VALUE", String(25), nullable=False)
    condition_type = Column("CONDITION_TYPE", String(25), nullable=False)
    is_pre_calc = Column("IS_PRE_CALC", Integer, nullable=False)  # 0 = False, 1 = True
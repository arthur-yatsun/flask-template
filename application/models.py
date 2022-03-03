from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType


from constants import Currency


Base = declarative_base()


class Transaction(Base):
    """Table to store transactions"""

    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(ChoiceType(Currency, impl=Integer()), nullable=False)
    value = Column(Numeric, nullable=False)
    description = Column(String(200), nullable=False)

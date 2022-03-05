from sqlalchemy import Column, Integer, Numeric, String, Index, DateTime, func
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import ChoiceType

from constants import Currency

Base = declarative_base()


class Transaction(Base):
    """Table to store transactions"""

    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(Numeric, nullable=False)
    currency = Column(ChoiceType(Currency, impl=Integer()), nullable=False)
    description = Column(String(200), nullable=False)

    # by default in UTC zone
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)


Index("transaction_currency_idx", Transaction.currency)

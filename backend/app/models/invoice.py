from sqlalchemy import Column, Integer, String, Float

from app.database import Base

class Invoice(Base):

    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)

    invoice_no = Column(String, unique=True)
    client_name = Column(String)

    amount = Column(Float)

    due_date = Column(String)

    email = Column(String)

    overdue_days = Column(Integer)

    followup_stage = Column(String)

    status = Column(String, default="Pending")
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    invoice_no = Column(String)

    client_name = Column(String)

    email = Column(String)

    stage = Column(String)

    subject = Column(String)

    send_status = Column(String)

    timestamp = Column(String)
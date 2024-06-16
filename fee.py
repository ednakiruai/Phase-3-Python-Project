from database import Base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class Fee(Base):
    __tablename__ = 'fee'
    id = Column(Integer, primary_key=True)
    fee = Column(String, nullable=False)
    fee_date = Column(Date, nullable=False)
    fee_amount = Column(Integer, nullable=False)
    fee_type = Column(String, nullable=False)
    fee_status = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    parent_id = Column(Integer, ForeignKey('parent.id'), nullable=False)

    student = relationship("Student", back_populates="fees")
    parent = relationship("Parent", back_populates="fees")

    def __init__(self, fee, fee_date, fee_amount, fee_type, fee_status, student_id, parent_id):
        self.fee = fee
        self.fee_date = fee_date
        self.fee_amount = fee_amount
        self.fee_type = fee_type
        self.fee_status = fee_status
        self.student_id = student_id
        self.parent_id = parent_id
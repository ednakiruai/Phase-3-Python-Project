from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    parent_relationship = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)

    student = relationship("Student", back_populates="parents")
    fees = relationship("Fee", back_populates="parent")

    def __init__(self, name, address, email, phone, gender, occupation, parent_relationship, student_id):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.gender = gender
        self.occupation = occupation
        self.parent_relationship = parent_relationship
        self.student_id = student_id
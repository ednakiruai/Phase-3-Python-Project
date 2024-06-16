from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from database import session  
from student import Student  


class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    grade = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'))

    student = relationship("Student", back_populates="grades")

    def __init__(self, grade, student_id=None):
        self.grade = grade
        self.student_id = student_id

    @staticmethod
    def add_grade(student_name, grade_value):
       
        student = session.query(Student).filter_by(name=student_name).first()
        if student:
            grade = Grade(
                grade=grade_value,
                student_id=student.id)
            
            session.add(grade)
            session.commit()
            print("Success: Grade added successfully!")

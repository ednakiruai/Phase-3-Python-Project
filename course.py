from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    course_name = Column(String, nullable=False)
    course_code = Column(String, nullable=False)
    course_semester = Column(String, nullable=False)
    course_year = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    course_credits = Column(Integer, nullable=False)

    student = relationship("Student", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")

    def __init__(self, course_name, course_code, course_semester, course_year, description, course_credits):
        self.course_name = course_name
        self.course_code = course_code
        self.course_semester = course_semester
        self.course_year = course_year
        self.description = description
        self.course_credits = course_credits


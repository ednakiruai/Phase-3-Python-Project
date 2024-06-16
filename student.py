from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session
from course import Course

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    dob = Column(String, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'))

    enrollments = relationship("Enrollment", back_populates="student")
    grades = relationship("Grade", back_populates="student")
    courses = relationship("Course", back_populates="student")
    attendances = relationship("Attendance", back_populates="student")
    parents = relationship("Parent", back_populates="student")
    fees = relationship("Fee", back_populates="student")

    def __init__(self, name, dob, address, email, phone, gender, course_id=None):
        self.name = name
        self.dob = dob
        self.address = address
        self.email = email
        self.phone = phone
        self.gender = gender
        self.course_id = course_id

    @staticmethod
    def assign_course_to_student(course_name, student_id):
        course = session.query(Course).filter_by(course_name=course_name).first()
        if course:
            student = session.query(Student).filter_by(id=student_id).first()
            if student:
                student.course_id = course.id
                session.add(student)
                session.commit()

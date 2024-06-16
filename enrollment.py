from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session
from datetime import datetime
from student import Student

class Enrollment(Base):
    __tablename__ = 'enrollment'
    id = Column(Integer, primary_key=True)
    enrollment_date = Column(Date, nullable=False, default=datetime.now().date())
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __init__(self, enrollment_date, student_id, course_id):
        self.enrollment_date = enrollment_date
        self.student_id = student_id
        self.course_id = course_id

    @staticmethod
    def enroll_student_in_course(student_id, course_id, enrollment_date=None):
        if enrollment_date is None:
            enrollment_date = datetime.now().date()
        student = session.query(Student).filter_by(id=student_id).first()
        if student:
            enrollment = Enrollment(enrollment_date=enrollment_date, student_id=student_id, course_id=course_id)
            session.add(enrollment)
            session.commit()

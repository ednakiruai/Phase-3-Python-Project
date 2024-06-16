from sqlalchemy import Column, Integer, Date, Time, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, session
from datetime import datetime
from student import Student
from course import Course
from enrollment import Enrollment

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False, default=datetime.now().date())
    time = Column(Time, nullable=False, default=datetime.now().time())
    status = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)

    student = relationship("Student")
    course = relationship("Course")

    def __init__(self, date, time, status, student_id, course_id):
        self.date = date
        self.time = time
        self.status = status
        self.student_id = student_id
        self.course_id = course_id

    @staticmethod
    def record_attendance(student_id, course_id, status, date=None, time=None):
        if date is None:
            date = datetime.now().date()
        if time is None:
            time = datetime.now().time()
        if isinstance(time, str):
            time = datetime.strptime(time, '%I:%M%p').time()

        attendance = Attendance(date=date, time=time, status=status, student_id=student_id, course_id=course_id)
        session.add(attendance)
        session.commit()

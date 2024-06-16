from database import session, engine, Base
from student import Student
from course import Course
from enrollment import Enrollment
from datetime import datetime
from fee import Fee
from attendance import Attendance
from datetime import datetime
from grade import Grade
from parent import Parent


def user():
    print("1. Add Student")
    print("2. Add Course")
    print("3. Add Fee")
    print("4. Add Attendance")
    print("5. Add Grade")
    print("6. Add Parent")
    print("7. Exit")


    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        add_course()
    elif choice == 3:
        add_fee()
    elif choice == 4:
        add_attendance()
    elif choice == 5:
        add_grade()
    elif choice == 6:
        add_parent()
    elif choice == 7:
        exit()

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


def add_student():
    print("Please enter student information:")
    students_name = input('Name: ')
    students_dob = input('Date of Birth (YYYY-MM-DD): ')
    students_address = input('Address: ')
    students_email = input('Email: ')
    students_phone = input('Phone: ')
    students_gender = input('Gender: ')
    course_name = input("Enter course name : ")
    enrollment_date_str = input("Enter enrollment date (YYYY-MM-DD): ")
    enrollment_date = datetime.strptime(enrollment_date_str, '%Y-%m-%d')


    student = Student(
        name=students_name,
        dob=students_dob,
        address=students_address,
        email=students_email,
        phone=students_phone,   
        gender=students_gender,)

    session.add(student)
    session.commit()
    Student.assign_course_to_student(course_name, student.id)
    course = session.query(Course).filter_by(course_name=course_name).first()
    if course:
        Enrollment.enroll_student_in_course(student_id=student.id, course_id=course.id, enrollment_date=enrollment_date)

    print("Success:Student added successfully!")


def add_course():
    print("Please enter course information:")
    course_name = input('Name: ')
    course_code = input('Code: ')
    course_semester = input('Semester: ')
    course_year = input('Year: ')
    course_description = input('Description: ')
    course_credits = input('Credits: ')

    course = Course(
        course_name=course_name,
        course_code=course_code,
        course_semester=course_semester,
        course_year=course_year,
        description=course_description,
        course_credits=course_credits )
    
    session.add(course)
    session.commit()
    print("Success: Course added successfully!")


def add_enrollment():
    print("Please enter enrollment information:")
    enrollment_date_str = input('Date (YYYY-MM-DD): ')
    enrollment_date = datetime.strptime(enrollment_date_str, '%Y-%m-%d')

    enrollment = Enrollment(
        enrollment_date=enrollment_date)

    session.add(enrollment)
    session.commit()
    print("Success: Enrollment added successfully!")


def add_fee():
    print("Please enter fee information:")
    Total_fee = int(input("Enter Total_fee: "))
    fee_date_str = input("Enter fee date (YYYY-MM-DD): ")
    fee_amount = int(input("Enter fee amount: "))
    fee_type = input("Enter fee type: ")
    fee_status = input("Enter fee status: ")
    student_name = input("Enter student name to link fee to: ")
    parent_name = input("Enter parent name: ")

    student = session.query(Student).filter_by(name=student_name).first()
    parent = session.query(Parent).filter_by(name=parent_name).first()
    fee_date = datetime.strptime(fee_date_str, '%Y-%m-%d').date()


    if student and parent:
        fee_instance = Fee(
            fee=Total_fee,
            fee_date=fee_date,
            fee_amount=fee_amount,
            fee_type=fee_type,
            fee_status=fee_status,
            student_id=student.id,
            parent_id=parent.id
        )

        session.add(fee_instance)
        session.commit()
    print("Success: Fee added successfully!")


def add_attendance():
    print("Please enter attendance information:")
    student_name = input("Enter student name: ")
    course_name = input("Enter course name: ")
    status = input("Enter attendance status (present/absent): ")
    date_str = input("Enter date (YYYY-MM-DD) : ")
    time_str = input("Enter time (HH:MM AM/PM): ")
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    time = datetime.strptime(time_str, '%I:%M %p').time()

    student = session.query(Student).filter_by(name=student_name).first()
    course = session.query(Course).filter_by(course_name=course_name).first()
    enrollment = session.query(Enrollment).filter_by(student_id=student.id, course_id=course.id).first()
    Attendance.record_attendance(student_id=student.id, course_id=course.id, status=status, date=date, time=time)
    print("Success: Attendance recorded successfully!")


def add_grade():
    print("Please enter grade information:")
    student_name = input('Student Name: ')
    grade_value = input('Grade: ')

    Grade.add_grade(student_name, grade_value)
    print("Success: Grade added successfully!")


def add_parent():
    print("Please enter parent information:")
    parent_name = input("Enter parent name: ")
    parent_address = input("Enter parent address: ")
    parent_email = input("Enter parent email: ")
    parent_phone = input("Enter parent phone: ")
    parent_gender = input("Enter parent gender: ")
    parent_occupation = input("Enter parent occupation: ")
    parent_relationship = input("Enter parent relationship to student: ")
    student_name = input("Enter the name of the student to link this parent to: ")

    student = session.query(Student).filter_by(name=student_name).first()
    parent = Parent(
        name=parent_name,
        address=parent_address,
        email=parent_email,
        phone=parent_phone,
        gender=parent_gender,
        occupation=parent_occupation,
        parent_relationship=parent_relationship,
        student_id=student.id
    )

    session.add(parent)
    session.commit()
    print("Success: Parent added successfully!")



if __name__ == "__main__":
    user()

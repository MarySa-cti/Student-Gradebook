from student import Student
from course import Course
from assessment import Quiz, Exam, Project
from gradebook import Gradebook

gradebook = Gradebook()

while True:

    print("\n===== Student Gradebook Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Add Course")
    print("4. Enroll Student in Course")
    print("5. Add Assessment")
    print("6. Record Grade")
    print("7. View Student Report")
    print("8. Search Student")
    print("9. Update Student Email")
    print("10. Delete Student")
    print("0. Exit")

    choice = input("Choose an option: ")

    # Add student

    if choice == "1":

        student_id = input("Student ID: ")
        name = input("Student Name: ")
        email = input("Email: ")

        student = Student(student_id, name, email)
        gradebook.add_student(student)

    # View Students
    elif choice == "2":

        if len(gradebook.students) == 0:
            print("No students found.")
        else:
            for student in gradebook.students.values():
                student.display_info()

    # Add course
    elif choice == "3":

        code = input("Course Code: ")
        name = input("Course Name: ")

        course = Course(code, name)

        gradebook.add_course(course)


    # Enroll student

    elif choice == "4":

        student_id = input("Student ID: ")
        course_code = input("Course Code: ")

        gradebook.enroll_student(student_id, course_code)


    # Add Assessments

    elif choice == "5":

        course_code = input("Course Code: ")

        print("\n1. Quiz")
        print("2. Exam")
        print("3. Project")

        assessment_type = input("Choose assessment type: ")

        title = input("Title: ")
        max_score = float(input("Maximum Score: "))

        if assessment_type == "1":
            assessment = Quiz(title, max_score)

        elif assessment_type == "2":
            assessment = Exam(title, max_score)

        elif assessment_type == "3":
            assessment = Project(title, max_score)

        else:
            print("Invalid assessment type.")
            continue

        gradebook.add_assessment(course_code, assessment)


    # Record grades

    elif choice == "6":

        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        title = input("Assessment Title: ")

        score = float(input("Student Score: "))

        gradebook.record_grade(student_id, course_code, title, score)

    # Student report

    elif choice == "7":

        student_id = input("Student ID: ")

        gradebook.show_report(student_id)

    # Search Student
    elif choice == "8":

        keyword = input("Enter student name or ID: ")

        gradebook.search_student(keyword)


   # Update the email

    elif choice == "9":

        student_id = input("Student ID: ")

        if student_id in gradebook.students:

            new_email = input("New email: ")

            gradebook.students[student_id].set_email(new_email)

        else:
            print("Student not found.")

    # Delete the student
    elif choice == "10":

        student_id = input("Student ID: ")

        gradebook.delete_student(student_id)

    # Exit
    elif choice == "0":

        print("Goodbye!")
        break

    else:

        print("Invalid choice. Please try again.")
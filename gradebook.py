from student import Student
from course import Course
from assessment import Quiz, Exam, Project

class Gradebook:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.grades = {}
        self.passing_grade = 55

    # Student_methods

    def add_student(self, student):
        if student.get_id() in self.students:
            print("Student ID already exists.")
        else:
            self.students[student.get_id()] = student
            print("Student added successfully.")

    def search_student(self, keyword):
        found = False

        for student in self.students.values():
            if keyword.lower() == student.get_id().lower() or keyword.lower() in student.get_name().lower():
                student.display_info()
                found = True

        if not found:
            print("Student not found.")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student not found.")
            return

        # Remove student from courses
        for course in self.courses.values():
            if student_id in course.students:
                course.students.remove(student_id)

        # Removing  grades

        if student_id in self.grades:
            del self.grades[student_id]

        del self.students[student_id]

        print("Student deleted successfully.")
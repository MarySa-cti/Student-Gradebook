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

# Course methods

    def add_course(self, course):
        if course.course_code in self.courses:
            print("Course already exists.")
        else:
            self.courses[course.course_code] = course
            print("Course added successfully.")

    def enroll_student(self, student_id, course_code):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        self.students[student_id].enroll_course(course_code)
        self.courses[course_code].add_student(student_id)

        print("Student enrolled successfully.")

    # Assessment methods

    def add_assessment(self, course_code, assessment):

        if course_code not in self.courses:
            print("Course not found.")
            return

        self.courses[course_code].add_assessment(assessment)

        print("Assessment added successfully.")

    # Grade methods

    def record_grade(self, student_id, course_code, assessment_title, score):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        assessment = self.courses[course_code].find_assessment(assessment_title)

        if assessment is None:
            print("Assessment not found.")
            return

        if score < 0 or score > assessment.max_score:
            print("Invalid score.")
            return

        if student_id not in self.grades:
            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = score

        print("Grade recorded successfully.")

    # Report methods

    def calculate_average(self, student_id, course_code):

        if student_id not in self.grades:
            return 0

        if course_code not in self.grades[student_id]:
            return 0

        course = self.courses[course_code]

        percentages = []

        for assessment in course.assessments:

            if assessment.title in self.grades[student_id][course_code]:
                score = self.grades[student_id][course_code][assessment.title]

                percentage = assessment.calculate_percentage(score)

                percentages.append(percentage)

        if len(percentages) == 0:
            return 0

        return sum(percentages) / len(percentages)

    def get_result(self, average):

        if average >= self.passing_grade:
            return "Passed"
        else:
            return "Failed"

    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        print("\n===== Student Report =====")
        print("Student ID:", student.get_id())
        print("Name:", student.get_name())
        print("Email:", student.get_email())

        if student_id not in self.grades:
            print("No grades recorded.")
            return

        for course_code in self.grades[student_id]:

            course = self.courses[course_code]

            print(f"\nCourse: {course.course_code} - {course.course_name}")

            for assessment in course.assessments:

                if assessment.title in self.grades[student_id][course_code]:
                    score = self.grades[student_id][course_code][assessment.title]

                    percentage = assessment.calculate_percentage(score)

                    print(
                        f"{assessment.title}: "
                        f"{score}/{assessment.max_score} "
                        f"({percentage:.2f}%)"
                    )
                    average = self.calculate_average(student_id, course_code)

                    print(f"Average: {average:.2f}%")
                    print("Result:", self.get_result(average))



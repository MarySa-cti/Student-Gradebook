class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.__email = email
        self.courses = []

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email = email
            print("Email updated successfully.")
        else:
            print("Invalid email.")

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)

    def display_info(self):
        print(f"\nStudent ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.__email}")
        print("Courses:", ", ".join(self.courses) if self.courses else "None")


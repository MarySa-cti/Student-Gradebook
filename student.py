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
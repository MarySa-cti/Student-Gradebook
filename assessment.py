class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 55:
            return "Passed"
        else:
            return "Failed"

    def display_info(self):
        print(f"{self.title} - Max Score: {self.max_score}")


class Quiz(Assessment):

    def display_info(self):
        print(f"Quiz: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Great quiz result!"
        else:
            return "Needs more practice."


class Exam(Assessment):

    def display_info(self):
        print(f"Exam: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 55:
            return "Passed exam."
        else:
            return "Failed exam."

class Project(Assessment):

    def display_info(self):
        print(f"Project: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 90:
            return "Excellent project!"
        elif percentage >= 55:
            return "Nice, Project submitted."
        else:
            return "Project needs improvement."
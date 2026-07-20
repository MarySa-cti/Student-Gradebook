
## Name
Maryam Sawaby 

## project title.
Student_Gradebook 

## What your project does.
student gradebook  is a tool  that allows users/ teachers to add and add and view students, add courses, enroll students in those courses, create various assessments such as quizzes, exams and projects, also this project helps users to record student's grades for the assessments and provides a student report, and edit student's contact, calculate the average score, and determine passing and failing status of students. 

## How to run the project.
For running this student gradebook project you need to open the project in python or any other Python IDE. 
make sure all the project files are located in the same folder. (the project consists of 6 files; main.py, student.py, course.py, assessment.py, gradebook.py and a README.md). 
then run the project from main.py. The program gives you a list of functions/ tasks the student gradebook can do, choose any option and enter the required details or view the provided info.  

## Which classes you created. 
This project has 7 classes total which are; 
Student
 Course
 Assessment
 Quiz
 Exam
 Project
gradebook. 

## Where you used encapsulation, inheritance, and method overriding.
## Encapsulation:
I used encapsulation in the Student class using __email, to make the email attribute private. I used getter and setter (get_email() and set_email()) methods to access and update the student`s email address safely. 
## Inheritance:
In this project  I used inheritance in the Assessment.py file. The Quiz, Exam and Project classes inherit from the Assessment class which is the parent class and they reuse its common methods and attributes. 
## Overriding:
I used method overriding in the Quiz, Exam, and Project class. each of these child class inherits from the Assessment class overrides display_info() and grade_message() from the assessment class in order to provide behavior  and output specific to that assessment type. 

## Featured costumes 
the project has 2 custom features;  
1. letter grading.   
This feature converts the student's final course grade into letter grade.   
A= 90-100   
B= 80-89   
C= 70-79   
D=60-69   
F= below 60.FAILED.
2. Teacher Comment:  
This feature provides a comment from the teacher based on the student`s final grade and the students with higher grades receive more positive feedback and for students with lower grades it sends an encouraging comment to improve their grades. 


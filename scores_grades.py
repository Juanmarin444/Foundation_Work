import random

def auto_grading(students):

    for student in students:

        grade = student['Grade']
        if grade >= 90:
            print "Student: ", student['Student'], "Score: ", grade, "; Your grade is A."
            continue
        if grade <= 89 and grade >= 80:
            print "Student: ", student['Student'], "Score: ", grade, "; Your grade is B."
            continue
        if grade <= 79 and grade >= 70:
            print "Student: ", student['Student'], "Score: ", grade, "; Your grade is C."
            continue
        if grade <= 69 and grade > 60:
            print "Student: ", student['Student'], "Score: ", grade, "; Your grade is D."
            continue
        if grade <= 59:
            print "Student: ", student['Student'], "Score: ", grade, "; Your grade is F." 
            continue

def students_testing():
    students = []

    for student in range(1,32):

        grade = random.randint(1,100)
        graded_students = {"Student": student, "Grade": grade }
        students.append(graded_students)

    return students
    # print students

students_testing()

auto_grading(students_testing())
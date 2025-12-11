import numpy as np


def print_student(student):
    print("Student name is " + student.name)
    print("ID is : " + student.id)
    print("DoB is : " + student.dob)


def print_course(course):
    print("Course name is " + course.name)
    print("ID is : " + course.id)
    print("credit is : " + str(course.credit))


def print_students(student_list):
    for i in student_list:
        print_student(i)
        print("----------------------------")


def print_courses(course_list):
    for i in course_list:
        print_course(i)
        print("-----------------------------")


def print_mark(marks):
    for i in marks:
        print(f"Student name: {i.student.name}, id: {i.student.id},dob : {i.student.dob},score:{i.student.gpa}")
        print(f"Course name : {i.course.name}, id : {i.course.id}, credit :{i.course.credit}")
        print(f"mark of {i.student.name} is: {i.mark}")


def cal_gqa_student(stu, marks):
    score = []
    credit = []
    for m in marks:
        if m.student == stu:
            score.append(m.mark)
            credit.append(m.course.credit)
    score = np.array(score)
    credit = np.array(credit)
    if len(score) == 0:
        return 0
    gpa = (score * credit).sum() / credit.sum()
    return gpa


def cal_gpa_students(students, marks):
    for stu in students:
        stu.gpa = cal_gqa_student(stu, marks)


def print_student_with_gpa(students):
    print("--------gpa of student --------")
    for stu in students:
        print(f"{stu.name} (id: {stu.id}) -> GPA = {stu.gpa:.2f}")
    print("---------------------------")


def sort_gpa(students):
    n = len(students)
    for i in range(n):
        for j in range(n - 1):
            if students[j].gpa < students[j + 1].gpa:
                students[j], students[j + 1] = students[j + 1], students[j]
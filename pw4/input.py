import math
from domains.student import Student
from domains.course import Course
from domains.mark import Mark


def input_student():
    name = input("name student : ")
    id = input("id of student: ")
    dob = input("dob of student: ")
    s = Student(name, id, dob)
    return s


def input_course():
    name = input("name course: ")
    id = input("id of course: ")
    credit = int(input("credit is: "))
    c = Course(name, id, credit)
    return c


def input_mark(students, courses):
    marks = []
    for student in students:
        for course in courses:
            mark_value = float(input(f"Input mark of student {student.name} in course {course.name} : "))
            mark_value_round = math.floor(mark_value)
            marks.append(Mark(student, course, mark_value_round))
    return marks


def input_courses():
    course_list = []
    num_cour = int(input("input your course: "))
    for i in range(num_cour):
        print("input your course" + str(i + 1))
        course = input_course()
        course_list.append(course)
    return course_list


def input_students():
    student_list = []
    num_student = int(input("number of student: "))
    for i in range(num_student):
        print("input your student" + str(i + 1))
        student = input_student()
        student_list.append(student)
    return student_list
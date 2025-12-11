from input import input_students, input_courses, input_mark
from output import cal_gpa_students, sort_gpa, print_student_with_gpa


def main():
    students = input_students()
    courses = input_courses()
    marks = input_mark(students, courses)
    print("-------------------")
    cal_gpa_students(students, marks)
    sort_gpa(students)
    print_student_with_gpa(students)


if __name__ == "__main__":
    main()
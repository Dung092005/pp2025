students = []
courses = []      # chỉ có 
mark = {}

def input_info_student():
    student_id = input("Enter student id : ")
    student_name = input("Enter student name : ")
    dob = input("Enter date of birtd : ")

    students.append({
        "id" : student_id, "name" : student_name, "dob" : dob
    })

def input_student():
    n = int(input("Enter number of student : "))
    for i in range(n):
        input_info_student()
    print("\n input successfully")

def input_info_course():
    n = int(input("Enter number of courses: "))
    for i in range(n):
        course_id = input("Enter couse id : ")
        course_name = input("Enter course name :")

        courses.append({
            "id" : course_id, "name" : course_name
        })

        mark[course_id] = []


def input_mark():
    course_id = input("Enter course id to input mark: ")

    # Kiểm tra course có tồn tại không
    if course_id not in mark:
        print("Course not found!")
        return

    # Nếu muốn nhập lại điểm thì có thể reset list:
    mark[course_id] = []

    # Nhập điểm cho từng sinh viên
    for student in students:
        a = float(input(f"Mark for student {student['name']} ({student['id']}): "))
        mark[course_id].append((student['id'], a))

    print("Input marks successfully!\n")

def print_info_student():
    for student in students:
        print("student id is : " + student['id'])
        print("student name is : " + student['name'])
        print("--------------------------- \n")

def print_info_courses():
    for course in courses:
        print("id of course is : " + course['id'])
        print("name of course is : " + course['name'])
        print("--------------------------- \n")

def print_mark():
    for course_id in mark:
        print("course id is " + course_id)
        for student_id,score in mark[course_id]:
            print(f"Student {student_id} -> Score {score}")
    


def menu():
    while True:
        print("---Student management-------")
        print("1.input student")
        print("2.input couses")
        print("3.input mark")
        print("4.list students")
        print("5.list courses")
        print("6.show mark for a course")
        print("0.quit")
        choice = input("choose your option you want : ")
        if choice == "1" :
            input_student()
        if choice == "2":
            input_info_course()
        if choice == "3":
            input_mark()
        if choice == "4":
            print_info_student()
        if choice == "5":
            print_info_courses()
        if choice == "6":
            print_mark()
        if choice =="0":
            break
        else:
            print("invalid option")

menu()

     
# n = int(input())

# id = int(input())

# name = str(input())

# Dob = str(input())

# nb_course = int(input())

# id_course = str(input())

# name_course = str(input())

students = []
courses = []
marks = {}

def input_number_student():
    print("Enter the nb of student: ")
    nb_student = int(input())
    for i in range(nb_student):
        print("Student ", i+1)
        input_info_student()

def input_info_student():
    students.append({"name": input("Name: ") , "id": input("ID: "),"Dob":input("Dob: ")})

def input_nb_course():
    nb_course = int(input("Input the nb of course: "))
    for i in range(nb_course):
        input_info_course()

def input_info_course():
    courses.append({"ID": input("ID course: "), "Name": input("Name_course: ")})

def input_mark():
    print("---INPUT MARK---")
    cid = input("Enter id of course: ")
    for course in courses:
        if cid == course["ID"]:
            for student in students:
                sid = student["id"]
                marks[(sid,cid)] = float(input("Enter mark: "))

def list_course():
    print("-----COURSE---------")
    for c in courses:
        print(f"ID: {c["ID"]} || Name: {c["Name"]}")
def list_students():
    print("------STUDENTS-------")
    for s in students:
        print(f"ID: {s["id"]} || Name: {s["name"]} || DoB: {s["Dob"]}")

def show_mark():
    for c in courses:
        


input_number_student()    
input_nb_course()
input_mark()

list_course()
list_students()
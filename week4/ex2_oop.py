class student:     
    def __init__(self, name, id, dob):         
        self.id = id         
        self.name = name         
        self.dob = dob 

class course:     
    def __init__(self, name, id):         
        self.id = id         
        self.name = name  

class mark:     
    def __init__(self, student, course, mark):         
        self.student = student         
        self.course = course         
        self.mark = mark  

def input_student():     
    name = input("name student : ")     
    id = input("id of student: ")     
    dob = input("dob of student: ")     
    s = student(name, id, dob)     
    return s 

def input_course():     
    name = input("name course: ")     
    id = input("id of course: ")     
    c = course(name, id)     
    return c  

def input_mark(students, courses):     
    marks = []      
    for student in students:         
        for course in courses:             
            mark_value = float(input(f"Input mark of student {student.name} in course {course.name} : "))             
            marks.append(mark(student, course, mark_value))     
    return marks 

def input_courses():     
    course_list = []     
    num_cour = int(input("input your course: "))     
    for i in range(num_cour):         
        print("input your course"+str(i+1))         
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

def print_student(student):     
    print("Student name is " + student.name)     
    print("ID is : " + student.id)     
    print("DoB is : " + student.dob)  

def print_course(course):     
    print("Course name is " + course.name)     
    print("ID is : " + course.id)  

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
        print(f"Student name: {i.student.name}, id: {i.student.id},dob : {i.student.dob}")         
        print(f"Course name : {i.course.name}, id : {i.course.id}")         
        print(f"mark of {i.student.name} is: {i.mark}")  

students = input_students() 
courses = input_courses() 
marks = input_mark(students, courses) 
print("-------------------") 
print_mark(marks)

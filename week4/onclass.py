class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def hello(self):
        print(f"hellp world from name {self.name}")
    def __str__(self):
        return f"{self.name},[{self.id}]"


student1 = student("dung","23ba14068")
student1.hello()
print(student1)

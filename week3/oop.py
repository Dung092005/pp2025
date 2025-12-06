class person1:
    def print(self):
        print("Name : ", self.name)
        print("Age",self.age)
    def __init__(self,n,a):
        self.name = n 
        self.age = a

macron = person1("Emmanuel macron",30)




# chứng tỏ vị chí hàm def print và __init__ ko ảnh hưởng 


class person2:
    def __init__(self, n,a):
        self.name = n
        self.age = a
    def describe(self):
        print("Name: ",self.name)
with open("data.txt","w") as file:
    file.write("a \n")
    file.write("b \n")
    file.write("c \n")
    file.write("d \n")
    file.write("e \n")

with open("data.txt","r") as file:
    data = file.read().split("\n")


data.pop()
print(data)

for i in data:
    print(i)    


# cách viết vào file io từ list 
students = ["An", "Bình", "Cường"]

with open("data.txt", "w", encoding="utf-8") as f:
    for s in students:
        f.write(s + "\n")   # khi bạn write mà ko dùng a thì tất cả cái đã viết trc đều bị delete

# write from interger to 0 in data.txt
user = int(input())
with open("data.txt","w") as f:
    for _ in range(user):
        f.write(str(user -_) + "\n") 



    

print('abc' + '123')

# multiple 

print('hi' * 5)

#in và not in 

print("us" in "amongus")

print("us" not in "amongus") 


s = "advanced prigramming with python" 
print(s[:20])
print(s[-6:-4])
print(s[-6:])

#string[index:end:step]


#format trong puton là để lấp cái parameter vào cái {},{}
name = "tiến Dũng"
age = 19
print("greeting,{}, you are {}".format(name,age))


name  = ["ICT", "ict"] 
print(type(name))
name = name + ["ict2"]


#replace element
name[1] = "i see tea"
print(name)

name[1:4] = ["icy tea ", "i see tea","tien dung"]
name[1:1] = ["ice city"]
#delete 1 element using: del

del name[1] 
print(name)
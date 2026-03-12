students=[["id","name","grade"],[1,"Ravi","O"],[2,"Mitesh","A+"]]
print(students)
# print(students[0])
# print(students[1])
# print(students[2])

# for i in students:
#     print(i)

#find student name and grade whose id is 2
# print("student id 2 name is=",students[2][1])
# print("student id 2 name is=",students[2][2])

# find student name and grade by entering student id 
id=int(input("enter student id to find name and grade="))
flag=False 
for i in students:
    if i[0]==id: 
     flag=True
     print("ID=",i[0])
     print("Name=",i[1])
     print("Grade=",i[2])

if flag==False:
   print("id not found. try again!!")
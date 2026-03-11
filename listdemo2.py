list1=[11,34,56,23,3,19]
print(list1)

# operation
x=[1,2,3]
y=[4,5,6]
print(x+y)
# print(x+100) #TypeError: can only concatenate list (not "int") to list
x.append(100)
print(x)
x[2]=222
print(x)
# x[7]=99  #IndexError: list assignment index out of range
print(x)

# methods
# Add elements into list append(),insert()
colors=[]
print(colors)
colors.append("red")
print(colors)
colors.append("green")
print(colors)
colors.append(["bule","white"])
print(colors)
print(colors[-1])
print(colors[2])
colors.append(("cyan","grey"))
print(colors)
colors.append({"black","yellow"})
print(colors)
colors.append({"#0ef455":"lightgreen"})
print(colors)

# update last element
colors[-1]="yellwo"
print(colors)

# add  element by using insert 
colors.insert(0,"orange")
print(colors)
print(len(colors))
colors.insert(11,"cream")
print(colors)



print(colors.index("cream"))


# delete element 
colors.pop()
print(colors)
colors.pop(2)
print(colors)
colors.remove("red")
print(colors)
del colors[0]
print(colors)


#traversind list 
for i in colors:
    print(i)

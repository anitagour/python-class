# Methods-> index(), append(),insert(),pop(),remove(),reverse(),sort(),copy(),clear(),count()
# for i in range(1,11):
#     print(i,end=" ")
# List comprehension
# syntax [output for iterable_variable in sequence_object if condition]

# print 1 to 10
# print([i for i in range(1,11)])

# print 1 to 10 square
# print([i*i for i in range(1,11)])

# for i in range(1,11):
#     if i%2==0:
#         print(i)
# print([i for i in range(1,11) if i%2==0])


#WAP to create mylist add number as per count enter very very importent 5
# mylist=[]
# or
# mylist=list()
# count=int(input("enter count for number="))
# for i in range(count):
#     number=int(input(f"enter {i+1} number="))
#     mylist.append(number)

# print(mylist)
# mylist_new=[input("enter number") for i in range(count)]
# print(mylist_new)


# WAP to show even and odd numbers seperately 
mylist=[12,4,2,67,256,600,2]
even=[]
odd=[]
print("Even Number=")
# for i in mylist:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# or

# [even.append(i) if i%2==0 else odd.append(i) for i in mylist]
# print("even nuer=",even)
# print("odd nuer=",odd)

# or
#  even=[i for i in mylist if i%2==0]
# odd=[i for i in mylist if i%2!=0]
# print("Even numbers=",even)
# print("Odd numbers=",odd)
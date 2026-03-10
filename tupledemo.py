# Tuple:collection different data elements enclosed into () parenthesis
# It is sequence,index follows, ordered but it i immutable

# create tuple 
tup=()
print(tup,type(tup))
t1=tuple()
print(t1,type,(t1))

t2=(500)
print(t2,type(t2))

t3=(500,100,"hello",True,5j,89.8789)
print(t3,type(t3))

# t4=tuple(78,89,90)# error 
t4=tuple((78,89,90))
print(t4,type(t4))


my_tuple=(3,45,64,6764,34,100)
print(my_tuple)

#index 
print("first element=", my_tuple[0])
print("last element=",my_tuple[-1])


# Slicing
print(my_tuple[::-1])
print(my_tuple[2:5])

# operation
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)
# print(tuple1+100)  # TypeError: can only concatenate tuple (not "int") to tuple


#tuple fuction 
tuple3=(1,5,4,2,3)
print(tuple3)
print(sorted(tuple3))
print(sorted(tuple3)[::-1])
print(sorted(tuple3,reverse=True))

#tuple method-index(),count()
tuple4=("hello","red","Orange","green", 1000,300,700)
# print(tuple.index(300))

# print(tuple4.index(3))  #ValueError: tuple.index(x): x not in tuple
print(tuple4.index(300))  # 5
print(tuple4.count(300)) #1

# immutablity
# tuple4[0]="welcome"  # TypeError: 'tuple' object does not support item assignment
print(tuple4) 

# Traversing of tuple
my_tup=(100,200,300,400,1,2,3)
# for i in my_tup:
#     print(i)

# for i in my_tup[::-1]:
#     print(i)

for i in sorted(my_tup):
    print(i)

for i in sorted(my_tup)[::-1]:
    print(i)
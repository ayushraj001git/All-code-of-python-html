# # Tuple unpacking

# st1 = ("Ravi",21,89)

# name,age,per_st1 = st1
# # print(name)
# # print(age)
# # print(per_st1)

# a = 10
# b = 20

# a,b=b,a

# print(a)
# print(b)

# l1 = [1,2,2,3,]
# t1 = (5,56,6,7)

# print(tuple(l1))
# print(type(tuple(t1)))
# print()
# print(list(t1))
# print(type(t1))

# Create a new list from an pre existing tuple where each of the new element of list should the cube of the elements of tuple if and only if the elements are odd. t1=(56,67,99,87,31,32)

# t2 = (56,67,99,87,31,32)
# l1_new = [i**3 for i in t2 if i%2 != 0]
# print(l1_new)

# Nasted loops
n = int(input("enter : "))
for i in range(1,n + 1):
    for j in range(1,i+1):
     print("*", end = " ")
    print()
# # #LOOPS

# # print("******range(1,-11)******")
# # for i in range(1,11):
# #     print(i)

# numn = int(input())
# for i in range(1,num +1):
#         print(i)
    
# name = str(input("name : "))
# for i in range(1,11):
#     print(name)

# t_num = int(input())

# for i in range(1,11):

#    print(f"{t_num} X {i} = {t_num*i}") 

# n = int(input("Pattern print"))
# for i in range(0,n+1):
#  print("*")

# n = str(input(""))
# for i in range(1,6):
#  print(f"{n*i}")

#no of rows
n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end = " ")
    print()

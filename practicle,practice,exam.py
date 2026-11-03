# n=int(input("enter number:"))
# factor=0
# for i in range(1,n+1):
#  if n%1 == 0:
#         factor +=1
# if factor==2:
#             print("prime number")
# # else:
# #     print("not a prime")

# m = float(input("enter meter:"))
# km= m/1000
# print(km,"km")

# km = float(input("enter kilometer:"))
# m = km*1000
# print(m,"m")

# n=int(input("enter a number:"))
# factor=0
# for i in range(1,n+1):
#     if n%1 == 0:
#         if factor==2:
#             print("prime number")
#         else:
#             print("not a prime")

# n=int(input("bata do"))
# print("even" if n%2==0 else "odd")


for i in range(2,51):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)
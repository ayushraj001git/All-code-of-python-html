# def hello(name="student"):
#     print("hello",name)

# hello("ravi")
# hello()

# Write a function to print all the elements items of a given list. L=[10,20,30,40,50]

# x = [10,20,30,40,50]

# def pl (l):
#     for i in range(len(l)):
#         print(l[i])
# x.append("harsh")

# pl(x)

# def pl(l):
#     for i in range (len(l)):
#         print(l[i], end = " ")
#     print()

# x = [10,20,30,40,50]

# x.append(90)
# pl(x)



# Write a turn to print all the digits of a given number {n = 7369}

n = int(input())
print()
def dp(n):
    while (n!=0):
        ld = n%10
        print(ld)
        n = n//10

dp(n)       




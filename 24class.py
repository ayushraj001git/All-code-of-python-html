# Recursion 
# def f(n):
#     if(n==11):
#         return
#     print(n)
#     f(n+1)

#     f(1)

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n*fact(n-1)

print(fact(5))
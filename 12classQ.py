# Take a input from user for a correct number until he/she guess`s it correctly.

# hidden
h = 10

# user guess

u_g = int(input("Enter your guess : "))

while(h != u_g):
    u_g = int(input("Enter your guess : "))
    print(f"{u_g} is the correct guess!!")

# (Q) Print all the digit of a given number(n)

n = int(input())
while(n == 0):
    last_digit = n%10
    print(last_digit)
    n = n//10
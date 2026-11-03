 # Q) Write a function validate the given password. include digit 8 to 12, small, cspital,special character $#&*^@/?, no space.

# import re

# def validate_password(password):
    
#     pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#&*^@/?])[^\s]{8,12}$"
    
#     if re.match(pattern, password):
#         return True
#     else:
#         return False

# # User input testing
# user_password = input("Apna password enter karein: ")

# if validate_password(user_password):
#     print("Password right hai! (Valid Password)")
# else:
#     print("Password wrong hai! (Invalid Password. Check length and required characters.)")


 # Q) Write a function to print each element of the given touple beside its index t=(10,20,30,40)

# def print_tuple(t):
#     for i in range(len(t)):
#         print(f"Index {i} : {t[i]}")

# t = (10, 20, 30, 40)
# print_tuple(t)


# Q) Write a function to calculate minimum, maximum, average

# def calculate(t):
#     mini = min(t)
#     maxi = max(t)
#     avg = int( sum(t) / len(t))

#     print(f"Minimum = {mini}")
#     print(f"Maximum = {maxi}")
#     print(f"Average = {avg}")


# t = (10, 20, 30, 40)
# calculate(t)

# Method 2

t = (10,20,30,40)
def min_max_avg(t):
    print(f"Minimum :{min(t)}")
    print(f"Maximum :{max(t)}")
    print(f"Average :{sum(t)//len(t)}")
min_max_avg(t)
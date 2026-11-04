x = int(input())
y = int(input())

def divide (a, b):
    a = int(a)
    b = int(b)
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: Denominator cannot be zero.")
    except ValueError:
        print("Error: Invalid input. Please enter whole numbers.")

divide(x, y)

























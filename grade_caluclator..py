# input
marks = int(input("Enter your marks :"))

# A Grade
if(marks >=90):
    print("Grade : A")

elif(marks>= 75 and marks<=89):
    print("Grade : B")
elif(marks>= 60 and marks<=74):
    print("C")
elif(marks>= 40 and marks<=59):
    print("D")
    #F
else:
    print("F")
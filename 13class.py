# Print all the number from 1 to n which are divisible by 5 & 3
n = int(input("Enter n:" ))
i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    i += 1

 # Count all the number from 1 to n which are divisible by 5 & 3
n = int(input("Enter n: "))
i = 1
count = 0

while i <= n:
         if i % 3 == 0 and i % 5 == 0:
             print(i)
             count += 1
             i += 1
             print("Count=", count)

# Check if the given number is perfect number or not
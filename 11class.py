n = int(input())

# counter
count = 0

for i in range(1,n+1):
    if(n%i == 0):
        count += 1

        #checck for prime
        if(count == 2):
            print(f"Given number {n} is a prime number")
        else:
            print(f"give nmumber {n} is not a prime number")
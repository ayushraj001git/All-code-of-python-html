# Q) Write a function to move all the zeros of the given list of the end, while mainting sequence.
# sample test case: [0,1,0,3,12]
# output: [1,3,12,0,0]

li=[1,3,5,0,1]
def f(l):
    non_zero = [i for i in l if i!=0]
    zero = [i for i in l if i == 0]
    print(non_zero + zero)
    f(l)
f(li)
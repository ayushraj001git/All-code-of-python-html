# Q) Write function to swap 1st and last element of a given tuple. t=(10,20,30,40,50) excepted output (50,20,30,40,10)

# t = (10,20,30,40,50,)

# def swap(t):
#     result = (t[-1],) + (t[1:-1]) + (t[0],)
#     return result
# print(swap(t))


#

# t = (10,)
# def swap(t):
#     if len(t) <2:
#         return t
#     result = (t[-1],) + (t[1:-1]) + (t[0],)
#     return result
# print(swap(t))



# Q) Write a function to rotate a given tuple by k positions. t=(10,20,30,40,50,60) k=2. expected output (50,60,10,20,30,40)

t = (10, 20, 30, 40, 50, 60)

def swap(t):
    def rotate(t,k):
        k = k%len(t)
        print(k)
        return[-k] + t[:-k]

        print(rotate(t,2))
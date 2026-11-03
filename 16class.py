str1 = "Apple"
a = 0
e = 0
i = 0
o = 0
u = 0

for i in str1:
    if("a" == i or "A" ==i):
        a+= 1
    elif("e" == i or"E" ==i):
        e+=1
    elif("i" == i or"I" ==i):
        e+=1
    elif("o" == i or"0" ==i):
        e+=1
    elif("u" == i or"U" ==i):
        e+=1
print("count of a:", a)
print("count of e:", e)
print("count of i:", i)
print("count of o:", o)
print("count of u:", u)

        
#Reverse a given string using a loop str1= "Ayush Aman"

str1 = "Ayush Aman"
x = str1[:: -1]

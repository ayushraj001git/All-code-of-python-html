list1 = [10,20,30,40,50,60,70,80,90,100]
list2 = ["Rungta",0.9,False,77]
print(list1)
tuple1 = (10,20,30,40,50,60,70,80,90,100)
print(tuple1)

print(max(list1))
print(min(list1))
# Adding an elementat the last of list
list1.append(110)
# Insert's an element at particular position
print(list1.insert(6,55))
print(list1)
print(list1.count(1))
print(list1.index(20))

li3 = [i for i in range (1,11)]
print(li3)


li4 = [i for i in range(50,101) if i%2 ==0]
print(li4)

li5 = [78,99,1010,"LI4",5.0]
for i in range(len(li5)):
    print(li5[i])
# Dictionary are of same length.
# Q) Write a function to merge add (d1,d2) and add the values of those key which are common in the given dictionary.
# sampletest
# d1={'a':1,'b':9}
# d2={'b':10,'c':7}
# merge add(d1,d2)
# output:{'a:1,'b':19 'c':7}

def merge_add(d1, d2):
    result = d1.copy()  
    
    for key, value in d2.items():
        if key in result:
            result[key] += value  
        else:
            result[key] = value  
            
    print(result)


d1 = {'a':1, 'b':9}
d2 = {'b':10, 'c':7}
merge_add(d1, d2)

from collections import Counter

def merge_add(d1, d2):
    print(dict(Counter(d1) + Counter(d2)))
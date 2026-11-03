# Q) Write a function to print the largest and second largest number in a given list. t = (99,70,20,110,80)
# Output:
#   largest no: 110
#   secondlargest: 99


# def largest_2nd(t):
#     a, b = 0, 0
#     for n in t:
#         if n > a:
#             b, a = a, n
#         elif n > b:
#             b = n
#     print(f"largest no: {a}\nsecondlargest: {b}")

# t = (99,70,20,110,80)
# largest_2nd(t)



# Q) Write a function check what elements gives the target sum in the given tuple:
# sample test case:
# target = 9
# t = (1,2,3,1,4,5,8)

def find_pairs(t, target):
    pairs = []
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] + t[j] == target:
                pairs.append((t[i], t[j]))
    return pairs


t = (1,2,3,1,4,5,8)
target = 9
print(find_pairs(t, target))
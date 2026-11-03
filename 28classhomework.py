s="this is a @Ayush $Raj12341"
def count_sen(n):
    count_vow=0
    count_cons=0
    count_number=0
    count_spaces=0
    count_spec=0
    vowel="aeiouAEIOU"
    for char in n:
        if char.isnumeric():
            count_number+=1
        elif char.isalpha():
            if char in vowel:
                count_vow+=1
            else:
                count_cons+=1
        elif char.isspace():
            count_spaces+=1
        else:
            count_spec+=1
    return count_number , count_vow, count_cons, count_spaces,count_spec
print(count_sen(s))
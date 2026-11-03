# Q) Write a function that removes duplicate character from the given string and print the new modified string s="Hello"



s = input()
clean_s = s.strip()

def remove_duplicataes(s):
    #empty string
    tem_empty = ""
    for i in s:
        if i not in temp_empty:
            temp_empty += i
            return temp_empty
        print(remove_duplicataes(clean_s))

# Q)
        clean_s = s.strip()
        def remove_duplicates(s):
            def swapcase(s):
                te = ""
                for i in s:
                    if i.isupper():
                        te += i.lower()
                    elif i.islower():
                        te += i.upper()
                    else:
                        te += i
                        return te
                    print(swapcase(clean_s))
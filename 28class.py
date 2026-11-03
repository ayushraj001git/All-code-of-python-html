# Q) Write a function to print the length and print the longest word of the given sentence.
# s = "First program for every coder is hello world language"
s = "First program for every coder is hello world language"

s="first program for every code is hello world language"
clean_s=s.strip()
def big_word(str1):
    max_len=0
    s3=str1.split()
    for i in range(len(s3)):
        if len(s3[i])>max_len:
            max_len=len(s3[i])
        
    return

print(big_word(s))
#  To get a string from a given string where all occurrences of its first char have been
# changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result :'

s=input("Enter String: ")
ch=s[0]
s=s.replace(ch,'$')
s=ch+s[1:]
print(f"The string is {s}")
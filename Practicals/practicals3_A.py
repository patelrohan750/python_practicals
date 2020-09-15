# A.To add 'ing' at the end of a given string (length should be at least 3). If the given string
# already ends with 'ing' then add 'ly' instead. If the string length of the given stringis less than
# 3, leave it unchanged.
# Sample String : 'abc' Sample String : 'string'
# Expected Result :'abcing' Expected Result: 'stringly'

s=input("Enter the String: ")
if len(s)>2:
    if s.endswith("ing"):
        s+="ly"
        print(s)
    else:
        s+="ing"
        print(s)
else:
    print("No change in String")

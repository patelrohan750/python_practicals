# Develop a python program to understand working of Execption handling
try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()

except IOError:
    print('file not found')
except Exception as e:
    print(e)
else:
    print("No exceptions")
finally:
    print("This will execute no matter what")
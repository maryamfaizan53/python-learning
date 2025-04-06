# file handling
# open a file
# read or write
# close a file

f = open("test.txt", "r")
print(f.read())
f.close()

f = open("test.txt", "w")
f.write("This is a test file")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()

# append a file
f = open("test.txt", "a")
f.write("This is a test file")
f.close()

f = open("test.txt", "r")   
print(f.read())
f.close()
# file handling with context manager
with open("test.txt", "r") as f:
    print(f.read())

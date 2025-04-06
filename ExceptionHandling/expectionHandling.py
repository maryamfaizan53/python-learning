#Exception Handling
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception as e:
    print("Can't divide a number by zero",e)
finally:
    print("Finally will execute every time")
    


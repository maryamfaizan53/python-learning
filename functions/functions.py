#python functions
def greet():
    print("Hello")
    print("Good Morning")
greet()

def add(x,y):
    c=x+y
    print(c)
add(5,4)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,4)
print(result1,result2)

    
    #types of fucntions in python
    #1. Built in function
    #2. User defined function
    #3. Lambda function
    #4. Recursive function
    #5. Anonymous function

def update(x):
    x=8
    print(x)
    
     
   #user defined function
def add(x,y):
    c=x+y
    print(c)
    
add(5,4)
def add_sub(x, y):
    c=x+y
    d=x-y
    return c,d
result1, result2=add_sub(5,4)

print(result1, result2)

#lambda function
f=lambda a:a*a
print(f(5))
#lambda function with multiple arguments    
f=lambda a,b:a+b
print(f(5,4))

#4. Recursive function

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1) 
    
    
print(factorial(5))
#5. Anonymous function
f=lambda a:a*a
print(f(5))
#Anonymous function with multiple arguments
f=lambda a,b:a+b
print(f(5,4))

     
#The Math & Date Time Calender
#This is a simple program that will help you to do math and date time calender
#It will help you to do math and date time calender 

#Getting the Current Time
import time
localtime = time.localtime(time.time())
print ("Local current time :", localtime)

#Getting the Calendar for a Month

import calendar
cal = calendar.month(2025, 1)
print ("Here is the calendar:")
print (cal)

#The Date Time
from datetime import date

date1 = date(2023, 4, 19)
print("Date:", date1)
date2 = date(2023, 4, 30)
print("Date2:", date2)



x = datetime.datetime.now() #The date contains year, month, day, hour, minute, second, and microsecond.
print(x)

#The strftime() Method
import datetime

x = datetime.datetime(2025, 1, 1)

print(x.strftime("%f")) #Display Microsecond 000000-999999
print(x.strftime("%A")) #Display the name of the Day
print(x.strftime("%Y")) #Display the Year
print(x.strftime("%B")) #Display the name of the month


#Python Math Module
import math

# abs() returns the absolute value of a number
# In Python, abs() is a built-in function, which means it's a global function
# available in the standard library without needing to import any specific modules.
# You can use it directly in your code.
print("abs(-5) = ", abs(-5))  # outputs: 5

# pow() raises a number to a power
print("pow(2, 3) = ", pow(2, 3))  # outputs: 8

# round() rounds a number to a specified number of decimal places
print("round(3.14159, 2) = ", round(3.14159, 2))  # outputs: 3.14

# max() returns the largest of a set of numbers
print("max(1, 2, 3, 4, 5) = ", max(1, 2, 3, 4, 5))  # outputs: 5

# min() returns the smallest of a set of numbers
print("min(1, 2, 3, 4, 5) = ", min(1, 2, 3, 4, 5))  # outputs: 1

# math.sin() returns the sine of an angle in radians
print("math.sin(math.pi/2) = ", math.sin(math.pi/2))  # outputs: 1.0

# math.cos() returns the cosine of an angle in radians
print("math.cos(0) = ", math.cos(0))  # outputs: 1.0

# math.tan() returns the tangent of an angle in radians
print("math.tan(math.pi/4) = ", math.tan(math.pi/4))  # outputs: 1.0

# math.sqrt() returns the square root of a number
print("math.sqrt(9) = ", math.sqrt(9))  # outputs: 3.0

# math.factorial() returns the factorial of a number
print("math.factorial(5) = ", math.factorial(5))  # outputs: 120

# math.log() returns the natural logarithm of a number
print("math.log(10) = ", math.log(10))  # outputs: 2.302585092994046

# math.log10() returns the base-10 logarithm of a number
print("math.log10(100) = ", math.log10(100))  # outputs: 2.0

# math.exp() returns the value of e raised to a power
print("math.exp(2) = ", math.exp(2))  # outputs: 7.38905609893065

# math.ceil() returns the smallest integer greater than or equal to a number
print("math.ceil(4.7) = ", math.ceil(4.7))  # outputs: 5

# math.floor() returns the largest integer less than or equal to a number
print("math.floor(4.7) = ", math.floor(4.7))  # outputs: 4

# math.pi is a constant representing the ratio of a circle's circumference to its diameter
print("math.pi = ", math.pi)  # outputs: 3.14159265359

# math.e is a constant representing the base of the natural logarithm
print("math.e = ", math.e)  # outputs: 2.718281828459045

# math.tau is a constant representing the ratio of a circle's circumference to its radius
print("math.tau = ", math.tau)  # outputs: 6.283185307179586

# math.inf is a constant representing infinity
print("math.inf = ", math.inf)  # outputs: inf

# math.nan is a constant representing "not a number"
print("math.nan = ", math.nan)  # outputs: nan
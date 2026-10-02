#Write a function greet() that prints "Hello, Python Learner!" when called.
'''
def greet():
    print("Hello, Python Learner!")
greet()
'''
#Write a function square(num) that returns the square of a given number. Test it with different numbers.
'''
def sqaure(num):
    sqr=num*num
    return sqr
print(sqaure(5))
'''
#Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".
'''
def full_name(first,last):
    print(first +" "+ last)
full_name("shwetha","nayak")
'''
#Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
def area(length,width=10):
    area=length*width
    return area
print(area(10))

#Write a lambda function that adds two numbers and test it.
sum=lambda a,b:a + b 
print(sum(2,3))

#Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.
numbers=[1,2,3,4,5]
sqares=list(map(lambda x: x**x ,numbers))
print(sqares)
'''The map() function applies the lambda x: x**2
 to each element of the list, 
 and list() converts the result back into a list.
 '''
#Write a recursive function factorial(n) that returns the factorial of a number.
def fact(n):
    if n==1:
        return n
    return n* fact(n-1)
print(fact(5))

#Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.
def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0
    else:
        # Recursive case
        return (n % 10) + sum_of_digits(n // 10)
    
print(sum_of_digits(123476))  

#Import the math module and use it to:
#Find the square root of 144
#Calculate sin(90°) (hint: use math.radians())

import math
print(math.isqrt(177))
print(math.sin(90))
print(math.radians(90))

#Install and import the requests module (if available) and use it to fetch data from "https://api.github.com".
# Step 1: Install requests (run this in your terminal or command prompt)
# pip install requests

# Step 2: Import requests in your Python script
import requests

# Step 3: Fetch data from GitHub API
response = requests.get("https://api.github.com")

# Step 4: Print the response (JSON format)
print(response.json())
#end of the part

#Write a function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. Observe whether the value persists across function calls.

def increment():
    counter=0
    counter=counter+1
    print(counter)
increment()
increment()
increment()
increment()

#Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
def multiply(a,b):
    '''this multiplies a and b'''
    c=a*b
    return c
multiply(5,8)
print(multiply.__doc__)

#Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
def fibonacci(n):
    if(n==0 or n==1):
        return n
    
    return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(6))

# Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.
def safe_divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    else:
        c=a/b
    return c
print(safe_divide(50,0))

#Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
import my_utils
print(my_utils.is_even(10))
print(my_utils.is_even(3))






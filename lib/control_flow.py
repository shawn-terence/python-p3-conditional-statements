#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    
    if (username == "admin"or username=="ADMIN")and password== "12345":
            print("Access granted")
            return("Access granted")
    else: 
        print("Access Denied")
        return("Access denied")
    pass
#admin_login("admin","12345")
def hows_the_weather(temperature):
    # your code here
    if temperature<40:
         print( "It's brisk out there!")
         return( "It's brisk out there!")
    elif temperature>40 and temperature<65:
         print("It's a little chilly out there!")
         return("It's a little chilly out there!")
    elif temperature>85:
         print( "It's too dang hot out there!")
         return( "It's too dang hot out there!")
    else:
         print("It's perfect out there!")
         return("It's perfect out there!")
    pass
#hows_the_weather(70)

def fizzbuzz(num):
    # your code here
    if((num%3==0)and (num%5==0)):
        print("FB")
        return("FizzBuzz")
    elif(num%5==0):
         print("B")
         return("Buzz")
    elif(num%3==0 ):
        print("F")
        return("Fizz")
    else:
         print("num")
         return(num)
       
    pass
fizzbuzz(13)
def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero!")
            return None
    else:
        print("Invalid operation!")
        return None
    pass

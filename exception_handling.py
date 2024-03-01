print("Expection handling")

try:
    a =int(input("Enter the value of a : ")) 
    b = int(input("Enter the value of b : ")) 
    print(a/b)
    
except ZeroDivisionError:                       # have to state what type of error is expected
    print("Number can not be divided by zero")
    
else:
    print("program executed successfully")
    
finally:
    print("this is finally block")
    
    
# exception handling with raise keyword
def age(n):
    if n < 18:
        raise ValueError("age should be greater than 18")
    else:
        print("you are eligible to vote")
try:
    inp = int(input("enter your age : "))
    age(inp)
except ValueError:
    print("Age is less than 18")

def addition(num1,num2):
    num1 += num2
    return num1
def subtraction(num1,num2):
    num1 -= num2
    return num1
def mul(num1,num2):
    num1 *= num2
    return num1
def division(num1,num2):
    num1 /= num2
    return num1

def module(num1,num2):
    num1 %= num2
    return num1

def default(num1,num2):
    return "Incorrect day"

switcher = {
    1: addition,
    2: subtraction,
    3: mul,
    4: division,
    5: module
    }

def switch(operation):
    return switcher.get(operation, default)()

print('''You can perform operation
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Module ''')

#Take input from user
choice = int(input("Select operation from 1,2,3,4 : "))

print (switch(choice))
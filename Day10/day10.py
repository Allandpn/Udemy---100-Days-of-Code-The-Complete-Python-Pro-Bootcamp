from day10_art import logo
from os import system


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,    
}

def calculator():
    operation = ""
    _continue = True
    print(logo)
    n1 = float(input("What-s the first number?: "))
    for n in operations:
        print(n)
    while _continue: 
        while operation not in operations:
            operation = input("What-s the operation?: ")
        n2 = float(input("What-s the second number?: "))  
        result = operations[operation](n1,n2)
        print(f"{n1} {operation} {n2} = {result}")
        operation = ""
        n1 = result
        get_continue = input(f"Type 'y' to continue calculating with {result}, or thype 'n' to exit.: ")
        if get_continue != 'y':
            _continue = False
            system('cls')
            calculator()

calculator()


    
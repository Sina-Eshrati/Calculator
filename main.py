from art import logo

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    continue_calc = 'y'
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    while continue_calc == 'y':
        operation_symbol = input("pick an operation: ")
        num2 = float(input("What's the new number? "))
        answer = operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        continue_calc = input(f"Type 'y' to continue with {answer}, or 'n' to start again. ")
    calculator()

calculator()
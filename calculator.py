# Creating a Calculator in Python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}
def calculator():
  should_continue = True

  num1 = float(input("What's the first number: "))

  for key in operations:
      print(key)

  while should_continue:

      operation_symbol = input('Pick an operation from the line above: ')

      num2 = float(input("What's the second number: "))

      calculation = operations[operation_symbol]

      answer = calculation(num1, num2)
      print(f'{num1} {operation_symbol} {num2} = {answer}  ')

      if input(f"Type 'y' to continue calculating with {answer} and 'n' start a new calculation: ") == 'y':
          num1 = answer
      else:
        should_continue = False
        calculator()

calculator()
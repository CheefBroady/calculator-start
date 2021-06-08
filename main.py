#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

# Grundrechenarten
operations = {
  "+": add, 
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  num1 = int(input("What`s the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  # 
  # num2 = int(input("What`s the second number?: "))
  # first_answer = calculator[operation_symbol](num1, num2)
  # print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  
  # last_answer = first_answer
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What`s the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    repeat = input(f"Type 'y' to continuer calculating with {answer}, or type 'n' to start a new calcualation. If you will finisch calculating type 'x': ")
    if repeat == "y" or repeat == "Y":
      num1 = answer
    elif repeat == "n" or repeat == "N":
      should_continue = False
      calculator()  
    else:
      return "GoodBye"

calculator()


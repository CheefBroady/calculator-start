



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


calculator = {
  "+": add, 
  "-": subtract,
  "*": multiply,
  "/": divide
}


num1 = int(input("What`s the first number?: "))
for symbol in calculator:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What`s the second number?: "))
first_answer = calculator[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

calc_again = True
last_answer = first_answer
while calc_again:
  repeat = input(f"Type 'y' to continue calculating with {last_answer}, or type 'n' to exit.: ")
  if repeat == "y" or repeat == "Y":
    operation_symbol = input("Pick another operation: ")
    new_num = int(input("What`s the nextnumber?: "))
    new_answer = calculator[operation_symbol](last_answer, new_num)
    print(f"{last_answer} {operation_symbol} {new_num} = {new_answer}")
    last_answer = new_answer
  else:
    print("Goodbye")
    calc_again = False
  




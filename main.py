



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

# print(calculator["+"](5, 99))

num1 = int(input("What`s the first number?: "))
num2 = int(input("What`s the second number?: "))


for symbol in calculator:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

def answer(n1, n2):
  return calculator[operation_symbol](n1, n2)


print(f"{num1} {operation_symbol} {num2} = {answer(num1, num2)}")


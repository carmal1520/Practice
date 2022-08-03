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

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

num1 = int(input("What's the first number?: "))


for key in operations:
    print(key)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))

# if operation_symbol == "+":
#     answer = add(num1, num2)
# if operation_symbol == "-":
#     answer = subtract(num1, num2)
# if operation_symbol == "*":
#     answer = multiply(num1, num2)
# if operation_symbol == "/":
#     answer = divide(num1, num2)

calcuation = operations[operation_symbol]
answer = calcuation(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
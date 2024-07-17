from logo import logo
print("welcome to the calculator")


def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mult(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2


operation = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}
print(logo)
num1 = int(input("choose a number\n"))
for o in operation:
    print(o)
should_continue = True
while should_continue:
    operations = input("choose an operation\n")
    num2 = int(input("choose a second number\n"))
    cal_function = operation[operations]
    answer = cal_function(num1,num2)
    print(f"{num1} {operations} {num2}=  {answer}")

    choice = input("do yoy want to go further with the calculation. for yes press 'Y' for no press 'N'")
    if choice == "Y":
        num1 = answer
    else :
        should_continue = False
        









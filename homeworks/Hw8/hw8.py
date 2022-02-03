print("Calculator")
print("Enter your example \n")

x = int(input("x = "))
symbol = input("Symbol (+,-,*,/): ")
y = int(input("y = "))
if symbol in ('+', '-', '*', '/'):
    if symbol == '+':
        c = x + y
        f = open("result.txt", "w")
        f.write(str(x) + str(symbol) + str(y) + "=" + str(c) + "\n")
        f.close()
    elif symbol == '-':
        c = x - y
        f = open("result.txt", "w")
        f.write(str(x) + str(symbol) + str(y) + "=" + str(c) + "\n")
        f.close()
    elif symbol == '*':
        c = x * y
        f = open("result.txt", "w")
        f.write(str(x) + str(symbol) + str(y) + "=" + str(c) + "\n")
        f.close()
    elif symbol == '/':
        if y != 0:
            c = x / y
            f = open("result.txt", "w")
            f.write(str(x) + str(symbol) + str(y) + "=" + str(c) + "\n")
            f.close()
        else:
            print("Division by zero!!!")
else:
    print("Invalid symbol!")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x, y = a, b
while y:
    x, y = y, x % y
lcm = (a * b) // x
print("LCM:", lcm)
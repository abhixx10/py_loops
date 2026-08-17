a = int(input("Enter a: "))
b = int(input("Enter b: "))
for i in range(a, b+1):
    if i % 7 == 0:
        print(i, end=" ")
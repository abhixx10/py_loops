count = 0
while True:
    n = int(input("Enter number (negative to stop): "))
    if n < 0:
        break
    count += 1
print("Positive numbers entered:", count)
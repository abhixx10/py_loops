largest = None
while True:
    n = int(input("Enter number (0 to stop): "))
    if n == 0:
        break
    if largest is None or n > largest:
        largest = n
print("Largest:", largest)
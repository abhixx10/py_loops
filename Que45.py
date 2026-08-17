n = int(input("Enter number: "))
sum = 0
temp = abs(n)
while temp > 0:
    sum += temp % 10
    temp //= 10
print("Sum of digits:", sum)
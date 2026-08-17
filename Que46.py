n = int(input("Enter number: "))
even_sum = 0
odd_sum = 0
temp = abs(n)
while temp > 0:
    digit = temp % 10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    temp //= 10
print("Even digit sum:", even_sum)
print("Odd digit sum:", odd_sum)
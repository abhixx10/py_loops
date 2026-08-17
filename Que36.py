n = int(input("Enter number: "))
rev = 0
temp = abs(n)
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if n < 0:
    rev = -rev
print("Reversed:", rev)
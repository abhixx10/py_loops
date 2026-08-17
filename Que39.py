n = int(input("Enter number: "))
temp = n
digits = len(str(n))
sum = 0
while temp > 0:
    sum += (temp % 10) ** digits
    temp //= 10
if sum == n:
    print("Armstrong number")
else:
    print("Not Armstrong")
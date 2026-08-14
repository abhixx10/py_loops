num = int(input("Enter number: "))
original = num
digits = len(str(num))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit ** digits
    num = num // 10
if sum == original:
    print("Armstrong number")
else:
    print("Not Armstrong number")
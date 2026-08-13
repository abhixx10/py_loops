n = int(input("Enter n: "))
sum_odd = 0
i = 1
while i <= n:
    sum_odd += i
    i += 2
print("Sum of odd numbers up to", n, ":", sum_odd)
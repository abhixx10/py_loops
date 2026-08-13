n = int(input("Enter n: "))
sum_even = 0
i = 2
while i <= n:
    sum_even += i
    i += 2
print("Sum of even numbers up to", n, ":", sum_even)
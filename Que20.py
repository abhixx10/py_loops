n = int(input("Enter number of terms: "))
a = 0
b = 1
sum = 0
for i in range(n):
    sum += a
    c = a + b
    a = b
    b = c
print("Sum:", sum)
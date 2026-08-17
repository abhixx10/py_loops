nums = list(map(int, input("Enter numbers separated by space: ").split()))
hcf = nums[0]
for num in nums[1:]:
    a, b = hcf, num
    while b:
        a, b = b, a % b
    hcf = a
print("HCF:", hcf)
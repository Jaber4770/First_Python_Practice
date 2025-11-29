def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print(result)

nums = [1, 2,3]
for n in nums:
    nums.append(n+1)
    if len(nums) > 6:
        break
print(nums)
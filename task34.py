nums = [1, 2, 3, 7, 8, 9]
pairs = [(a, b) for i, a in enumerate(nums) for b in nums[i+1:] if a + b == 10]
print(pairs)   
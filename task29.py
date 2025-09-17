nums = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]
a = [x for x in nums if nums.count(x) == 1]
print(a)
def find_two_sum(nums, target):
    seen = set ()
    for num in nums:
        complement = target-num
        if complement in seen:
            return (complement, num) 
        seen.add(num)
    return None
a = [10, 20, 30, 35]
target = 50
result = find_two_sum(a, target)

if result:
    print("pair found:{result}")
else:
    print("no pair found")

    
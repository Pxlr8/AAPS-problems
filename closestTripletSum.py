def closestTripletSum(arr, target):
    arr.sort()  
    n = len(arr)
    closest_sum = float('inf')

    for i in range(n - 2):  
        left, right = i + 1, n - 1  

        while left < right:  
            total = arr[i] + arr[left] + arr[right]  

            if abs(target - total) < abs(target - closest_sum):
                closest_sum = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total  

    return closest_sum  
arr = [-1, 2, 1, -4]
target = 1
print("Closest triplet sum:", closestTripletSum(arr, target))

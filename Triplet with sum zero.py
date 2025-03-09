def findTriplet(arr):
    arr.sort()
    n = len(arr)

    for i in range(n - 2):
        left, right = i + 1, n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                return True
            elif total < 0:
                left += 1
            else:
                right -= 1
    return False
arr = [-1,0,1,2,-1,-4]
if findTriplet(arr):
    print("Triplet exists")
else:
    print("No Triplet found")

        
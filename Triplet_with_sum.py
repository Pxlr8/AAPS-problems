def has_triplet_with_sum(arr, target):
    n = len(arr)
    for i in range (n - 2):
        for j in range(i + 1,n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True  
    return False                          
arr = [1, 2, 3, 2]
target = 9
print(has_triplet_with_sum(arr, target))

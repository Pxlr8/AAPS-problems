def has_triplet_with_sum(arr, target):
    n = len(arr)
    for i in range(n - 2):
        seen = set()
        curr_sum = target - arr[i]
        for j in range(i + 1, n):
            if (curr_sum - arr[j]) in seen:
                return True
            seen.add(arr[j])
    return False

arr = [1, 2, 3, 2]
target = 5
print(has_triplet_with_sum(arr, target))

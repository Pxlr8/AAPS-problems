def rotate_array(arr, k):
    n = len(arr)
    k = k % n  
    rotated_arr = arr[-k:] + arr[:-k]
    return rotated_arr

arr = [1,2,3,4]
k = 2  
result = rotate_array(arr, k)
print("Rotated Array:", result)

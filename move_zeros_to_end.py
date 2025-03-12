def move_zeros_to_end(arr):
    non_zero_index = 0  
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1  

arr = [0, 1, 9, 0, 0, 2, 7, 0, 6, 0, 9]
move_zeros_to_end(arr)
print(arr)

def print_number_of_time(arr):
    frequency = {}  
    
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1 
    
    for key, value in frequency.items():
        print(f"{key} appears {value} times")

arr = [2,4,5,5,7]
print_number_of_time(arr)

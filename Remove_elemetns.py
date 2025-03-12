def remove_duplicate_elements_arr(arr):
    unique_elements = []
    seen = set()  
    
    for num in arr:
        if num not in seen:
            unique_elements.append(num)
            seen.add(num) 
    
    return unique_elements

arr = [4,3,1,1,7,4,1,4,7,3]
result = remove_duplicate_elements_arr(arr)
print(result)
